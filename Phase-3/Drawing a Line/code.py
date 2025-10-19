import cv2

image = cv2.imread("Phase-3\Drawing a Line\python.png")

if image is None:
  print("Sorry sir Your Image is Not loaded")

else:
  print("Image loaded successfully!")
  pt1 = (50,100)
  pt2 = (300,100)
  color = (0,0,0)
  thickness = 4

  cv2.line(image ,pt1,pt2,color,thickness)

  cv2.imshow("Line Drawing",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()