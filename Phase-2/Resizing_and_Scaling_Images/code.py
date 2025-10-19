import cv2

image = cv2.imread("Phase-2\Resizing_and_Scaling_Images\logo.png")
if image is not None:
  print("Image Loaded Successfully!\n")
  resize = cv2.resize(image,(300,300))
  cv2.imshow("Resized image",resize)
  cv2.imshow("Original image",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
else:
  print("Image not found!")