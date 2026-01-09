import os
import urllib.request

MODEL_CFG = "yolov3-tiny.cfg"
MODEL_WEIGHTS = "yolov3-tiny.weights"
CLASS_NAMES_FILE = "coco.names"

def download_files():
    if not os.path.exists(MODEL_CFG):
        print(f"Downloading {MODEL_CFG}...")
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3-tiny.cfg", MODEL_CFG)
            print("Done.")
        except Exception as e: print(f"Failed to download {MODEL_CFG}: {e}")
    else:
        print(f"{MODEL_CFG} already exists.")
        
    if not os.path.exists(MODEL_WEIGHTS):
        print(f"Downloading {MODEL_WEIGHTS}...")
        try:
            urllib.request.urlretrieve("https://pjreddie.com/media/files/yolov3-tiny.weights", MODEL_WEIGHTS)
            print("Done.")
        except Exception as e: print(f"Failed to download {MODEL_WEIGHTS}: {e}")
    else:
        print(f"{MODEL_WEIGHTS} already exists.")

    if not os.path.exists(CLASS_NAMES_FILE):
        print(f"Downloading {CLASS_NAMES_FILE}...")
        try:
            urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names", CLASS_NAMES_FILE)
            print("Done.")
        except Exception as e: print(f"Failed to download {CLASS_NAMES_FILE}: {e}")
    else:
        print(f"{CLASS_NAMES_FILE} already exists.")

if __name__ == "__main__":
    download_files()
