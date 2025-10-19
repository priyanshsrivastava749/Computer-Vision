import cv2

image = cv2.imread("Phase-3\Drawing a Line\python.png")

if image is None:
  print("OOps the image is Not Loaded!")

else:
  print("The Image Loaded Successfully!")
  cv2.putText(image,"Hello World",(50,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),2)

  cv2.imshow("Adding Text over image",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
