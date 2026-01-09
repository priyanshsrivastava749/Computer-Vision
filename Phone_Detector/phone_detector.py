import cv2
import numpy as np
import subprocess
import os
import sys
import time

# --- Configuration ---
ASSETS_DIR = "assets"
AUDIO_FILE = "1.mp3"
CONFIDENCE_THRESHOLD = 0.6 # Increased to reduce false positives
NMS_THRESHOLD = 0.4
MODEL_CFG = "yolov3-tiny.cfg"
MODEL_WEIGHTS = "yolov3-tiny.weights"
CLASS_NAMES_FILE = "coco.names"
PHONE_CLASS_ID = 67  # COCO class ID for 'cell phone'

# --- Global Audio Cooldown ---
last_played_time = 0
AUDIO_COOLDOWN = 3
consecutive_detections = 0
REQUIRED_CONSECUTIVE_FRAMES = 5  # Must detect phone for 5 frames in a row to confirm

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get_sound_path():
    # ... (same as before) ...
    # Use absolute path to ensure file is found regardless of where script is run from
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(script_dir, ASSETS_DIR, AUDIO_FILE)
    
    print(f"[DEBUG] Looking for audio file at: {sound_path}")
    
    if not os.path.exists(sound_path):
        print(f"Error: Audio file not found at {sound_path}")
        return None
    return sound_path

def play_sound(sound_path):
    global last_played_time
    current_time = time.time()
    
    if current_time - last_played_time < AUDIO_COOLDOWN:
        return # Too soon
        
    print("Playing sound via PowerShell...")
    last_played_time = current_time
    
    # PowerShell command to play audio (fire and forget-ish via Popen)
    ps_command = f"""
    Add-Type -AssemblyName PresentationCore;
    $player = New-Object System.Windows.Media.MediaPlayer;
    $player.Open('{sound_path}');
    $player.Play();
    Start-Sleep -Seconds 2;
    """
    
    try:
        subprocess.Popen(["powershell", "-WindowStyle", "Hidden", "-Command", ps_command])
    except Exception as e:
        print(f"Error playing sound: {e}")

# --- Model Downloader (Simplified) ---
def check_and_download_files():
    files = [MODEL_CFG, MODEL_WEIGHTS, CLASS_NAMES_FILE]
    
    import urllib.request
    
    if not os.path.exists(MODEL_CFG):
        print(f"Downloading {MODEL_CFG}...")
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg", MODEL_CFG)
        except Exception as e: print(f"Failed to download {MODEL_CFG}: {e}")
        
    if not os.path.exists(MODEL_WEIGHTS):
        print(f"Downloading {MODEL_WEIGHTS}...")
        try:
            urllib.request.urlretrieve("https://pjreddie.com/media/files/yolov3-tiny.weights", MODEL_WEIGHTS)
        except Exception as e: print(f"Failed to download {MODEL_WEIGHTS}: {e}")

    if not os.path.exists(CLASS_NAMES_FILE):
        print(f"Downloading {CLASS_NAMES_FILE}...")
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names", CLASS_NAMES_FILE)
        except Exception as e: print(f"Failed to download {CLASS_NAMES_FILE}: {e}")

def main():
    global consecutive_detections
    check_and_download_files()
    
    # Load Model
    # Check bundled paths first, then local
    cfg_path = resource_path(MODEL_CFG)
    weights_path = resource_path(MODEL_WEIGHTS)
    names_path = resource_path(CLASS_NAMES_FILE)

    # If bundled files don't exist (dev mode), might rely on local files from download
    if not os.path.exists(cfg_path): cfg_path = MODEL_CFG
    if not os.path.exists(weights_path): weights_path = MODEL_WEIGHTS
    if not os.path.exists(names_path): names_path = CLASS_NAMES_FILE

    if not os.path.exists(weights_path) or not os.path.exists(cfg_path):
         print("Error: Model files missing. Cannot start detection.")
         return

    net = cv2.dnn.readNet(weights_path, cfg_path)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    
    if os.path.exists(names_path):
        with open(names_path, "r") as f:
            classes = [line.strip() for line in f.readlines()]
    else:
        classes = ["cell phone"]
        
    # Verify phone class ID
    try:
        phone_class_id = classes.index("cell phone")
    except ValueError:
        phone_class_id = 67
        
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    
    cap = cv2.VideoCapture(0)
    sound_path = get_sound_path()
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Phone detection started. Press 'q' to quit.")
    print("Architectured by Priyansh") 
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        height, width, channels = frame.shape

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                
                if confidence > CONFIDENCE_THRESHOLD and class_id == phone_class_id:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)

        phone_detected_now = False
        
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                confidence_val = confidences[i]
                
                # Double check class ID one more time just in case
                if class_ids[i] == phone_class_id:
                     phone_detected_now = True
                     
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {confidence_val:.2f}", (x, y - 5), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        if phone_detected_now:
            consecutive_detections += 1
            print(f"Phone detected! consecutive_frames={consecutive_detections}")
            if consecutive_detections >= REQUIRED_CONSECUTIVE_FRAMES:
                if sound_path:
                    play_sound(sound_path)
                # Cap the counter to avoid overflow or w/e, though python handles large ints
                # Just keep it at threshold to keep 'active' state
                consecutive_detections = REQUIRED_CONSECUTIVE_FRAMES 
        else:
            consecutive_detections = 0
        
        # Add Branding
        cv2.putText(frame, "Architectured by Priyansh", (10, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Phone Detector", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
