import cv2 

image = cv2.imread("Phase-2\Resizing_and_Scaling_Images\logo.png")

if image is None:
  print("Could not load image")

else: 
  (h,w) = image.shape[:2]

  center = (w//2,h//2)
  M = cv2.getRotationMatrix2D(center,90,1.0)
  rotated = cv2.warpAffine(image,M,(w,h))

  cv2.imshow("Original",image)
  cv2.imshow("Rotated 90 degree",rotated)
  cv2.waitKey()
  cv2.destroyAllWindows()