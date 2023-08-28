import cv2

img = cv2.imread("c:/Users/deepk/Downloads/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")

cv2.imshow("output",img)

cv2.waitKey(1)

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Mercury",(120,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Venus",(200,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Earth",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Mars",(380,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Jupiter",(550,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Saturn",(750,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Uranus",(980,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(img,"Neptune",(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)

cv2.imshow("output_with_text", img)

cv2.imwrite("solar_systemwithname.jpg",img)

cv2.destroyAllWindows()

