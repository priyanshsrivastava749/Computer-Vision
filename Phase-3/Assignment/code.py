import cv2

image = cv2.imread(input("Enter The location of the image: "))

if image is None:
  print("\nOOPS! no such image Exists")

else:
  print("\nImage loaded successfully")
  choice = input("\nEnter 1 for Drawing Line \nEnter 2 for Drawing a Circle\nEnter 3 for Drawing a Rectangle\nEnter 4 for Adding text to the image\n \n")

  if choice == "1":
    pt1 = tuple(map(int,input("\nEnter The First Point From where the line should begin: ").split()))
    pt2 = tuple(map(int,input("\nEnter the Coordinates for the Second point").split()))
    color = (0,0,0)
    thickness = 4
    cv2.line(image ,pt1,pt2,color,thickness)
    cv2.imshow("Line Drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  elif choice == "2":
    m,n = map(int,input("\nEnter the coordinate of Center of the circle: ").split())
    center = (m,n)
    radii = int(input("\nEnter the Radii!: "))
    cv2.circle(image,center,radii,(250,0,0),5)
    cv2.imshow("Image focusing rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  elif choice == "3":
    pt1 = tuple(map(int,input("\nEnter The First Coordinate: ").split()))
    pt2 = tuple(map(int,input("\nEnter the second coordinate: ").split()))
    color = (0,0,255)
    thickness = 3
    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("Image focusing window",image)
    cv2.waitKey()
    cv2.destroyAllWindows()
  elif choice == "4":
    text = input("\nEnter the Text to be added: ")
    point = tuple(map(int,input("Enter the coordinates: ").split()))
    cv2.putText(image,text,point,cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,0,0),2)
    cv2.imshow("Adding Text over image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#now asking user to save or reject the change...
save_choice = input("Do you wanna save changes or reject: ")
if save_choice == "yes":
  print("saved successfully")
  cv2.imwrite("Image_after_operation.png", image)
else:
  print("Execution completed!")