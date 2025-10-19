import cv2

image = cv2.imread("Phase-2\Resizing_and_Scaling_Images\logo.png")

if image is None:
  print("Could not load image")

else:
  flipped_horizontal = cv2.flip(image,1)
  flipped_vertical = cv2.flip(image,0)
  flipped_both = cv2.flip(image,-1)

  cv2.imshow("Original",image)
  cv2.imshow("flipped_horizontal",flipped_horizontal)
  cv2.imshow("flipped_vertical",flipped_vertical)
  cv2.imshow("flipped_both",flipped_both)
  cv2.waitKey()
  cv2.destroyAllWindows()
