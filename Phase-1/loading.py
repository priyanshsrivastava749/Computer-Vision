import cv2

image = cv2.imread("Phase-1\image.png")
if image is not None:
  cv2.imshow("Image showing",image) #open a new window
  cv2.waitKey(0) #hold on the new window till a key is being pressed
  cv2.destroyAllWindows()#close the window

else:
  print("Image could  not be loaded")


