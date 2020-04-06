import cv2

img=cv2.imread("cool.jpg",1)

# print(type(img))
# print(img)
resized_image=cv2.resize(img,(500,500))
resized_image2=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("R&M",img)
cv2.waitKey(0)
cv2.imshow("R&M2",resized_image)
cv2.waitKey(0)
cv2.imshow("R&M3",resized_image2)
cv2.imwrite("R&M_Resize.jpg",resized_image2)
cv2.waitKey(0)