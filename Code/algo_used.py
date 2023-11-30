import cv2
import numpy as np



img = cv2.imread('real9.jpeg')
im = img.copy()

hsv = cv2.cvtColor( img , cv2.COLOR_BGR2HSV)
l_b = np.array([36, 25 , 25]) #100 , 255 ,0
u_b = np.array([70 , 255 ,255])
l_b1 = np.array([78,154,40]) #[78,154,40
u_b1 = np.array([140,255,255]) #[167,255,150]



mask = cv2.inRange(hsv , l_b , u_b)
eroded = cv2.erode(mask , kernel=(13,13))
mask1 = cv2.inRange(hsv , l_b1 , u_b1)
x , y , w , h = cv2.boundingRect(mask)
x1 = 0
y1 = 0
w1 =0 
h1 =0 

a = [0 , 0 ,0 ,0]
contours, _ = cv2.findContours(mask1 , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
contours1, _ = cv2.findContours(mask, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)



for c1 in contours1:
    (x, y, w ,h) = cv2.boundingRect(c1)
    

    if cv2.contourArea(c1) < 15000:
     continue
    x1 = x
    y1 = y
    w1 = w
    h1 = h
    cv2.rectangle(img , (x1, y1) , (x1+w1, y1+h1), (0,0 , 0) , 2)


print(x1 , y1,w1 ,h1)

for c in contours:
 if cv2.contourArea(c)< 5000:
     continue
 approx = cv2.approxPolyDP(c , 0.01* cv2.arcLength(c , True) , True)
 cv2.drawContours(img , [approx] , 0 , (0,0,255) , 5)
 M = cv2.moments(c)
 if M["m00"] !=0:
  cx = int(M["m10"]/M["m00"])
 else:
     cx =0
 print(cx)
 if x1 < cx < (x1 +(w1/4)):
     a[0] = 1
 elif x1 <cx < (x1+(w1/2)):
     a[1] =1
 elif x1<cx < (x1+((3*w1)/4)):
     a[2] =1
 elif x1<cx < (x1+w1):
     a[3] =1
 else :
     continue


 
n = (8*a[0]) +( 4*a[1]) + (2*a[2]) + a[3]
Number = "Number =" + str(n)

cv2.putText(img , Number , (10, 200) , cv2.FONT_HERSHEY_SIMPLEX , 1.0 , (255 , 0, 0) , 2)

#cv2.imshow('image' ,mask2)
cv2.imshow('image2' ,img)



cv2.waitKey(0)
cv2.destroyAllWindows()