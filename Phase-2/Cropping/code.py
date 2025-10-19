import cv2

image = cv2.imread("Phase-2\Resizing_and_Scaling_Images\logo.png")

if image is not None:
  print("Image loaded successfully...")
  cropped = image[100:200,50:150]
  cv2.imshow("Original Img",image)
  cv2.imshow("cropped image",cropped)
  cv2.waitKey()
  cv2.destroyAllWindows()

