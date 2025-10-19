import cv2

imageadress = input("Enter the adress of image: ")
image = cv2.imread(imageadress)

if image is not None:
  print("The image is loaded successfully Now converting it to Gray form\n")
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  option = input("Enter a for displaying image or b to save it: ")
  if option == 'a':
    cv2.imshow("Output image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  elif option == 'b':
    outputname = input("Enter the name of the output image")
    cv2.imwrite(outputname,gray)

print("Program executed successfully!")


