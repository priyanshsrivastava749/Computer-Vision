import cv2

image = cv2.imread("Phase-3/Drawing a Line/python.png")

if image is None:
  print("Ooops! Theres no Image")
else:
  print("Image Loaded Successfully!")

  cv2.circle(image,(250,150),50,(250,0,0),5)
  cv2.imshow("Image focusing rectangle",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()