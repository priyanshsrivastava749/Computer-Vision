import cv2

image = cv2.imread("Phase-3\Drawing a Line\python.png")

if image is None:
  print("OOPS! Your Image Is not Working")

else:
  print("Image loaded successfully!")
  pt1 = (50,50)
  pt2 = (250,200)
  color = (0,0,255)
  thickness = 3
  cv2.rectangle(image,pt1,pt2,color,thickness)
  cv2.imshow("Image focusing window",image)
  cv2.waitKey()
  cv2.destroyAllWindows()