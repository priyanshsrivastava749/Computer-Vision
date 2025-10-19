import cv2

image = cv2.imread("Phase-1\image.png")

if image is not None:
  h, w, c = image.shape #this parameter is used to get the image shape means width height and color channel
  print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")

else:
  print("Ah sorry no image found!")
