import cv2
import numpy as np
from matplotlib import pyplot as plt

def numberdet(image):
    hsv = cv2.cvtColor( image , cv2.COLOR_BGR2HSV)
    l_b = np.array([20, 50 , 40]) #100 , 255 ,0
    u_b = np.array([70 , 255 ,255])
    l_b1 = np.array([80,160,45]) #[78,154,40
    u_b1 = np.array([140,255,255]) #[167,255,150]



    mask = cv2.inRange(hsv , l_b , u_b)

    mask1 = cv2.inRange(hsv , l_b1 , u_b1)


    a = [0 , 0 ,0 ,0]
    contours, _ = cv2.findContours(mask1 , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
    contours1, _ = cv2.findContours(mask, cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)







    circlex = []
    circley = []

    no = 0
    for c in contours:
        if cv2.contourArea(c)< 50:
            continue
        approx = cv2.approxPolyDP(c , 0.01* cv2.arcLength(c , True) , True)
        #cv2.drawContours(img , [approx] , 0 , (0,0,255) , 5)
        M = cv2.moments(c)
        if M["m00"] !=0:
            cx = int(M["m10"]/M["m00"])
            cY = int(M["m01"] / M["m00"])

        else:
            cx =0
            cY =0
        no = no +1
        circlex.append(cx)
        circley.append(cY)
    

    check =0
    for c1 in contours1:
        (x , y , w ,h) = cv2.boundingRect(c1)
        for i in range(0 , no , 1):
            if x < circlex[i] < x+w and y < circley[i] < y+h:
                #cv2.rectangle(img , (x, y) , (x+w,y +h), (0,0 , 0) , 2)
                check =1 
                if x <circlex[i]  < (x +(w/4)):
                  a[0] = 1
                elif x <circlex[i] < (x+(w/2)):
                  a[1] =1
                elif x<circlex[i] < (x+((3*w)/4)):
                  a[2] =1
                elif x<circlex[i] < (x+w):
                  a[3] =1
            else :
                continue
        if check == 1:
         break


    
    n = (8*a[0]) +( 4*a[1]) + (2*a[2]) + a[3]
    Number = "Number =" + str(n)  
    return Number  

img = cv2.imread('real4.jpeg')
img1 = cv2.imread('real1.jpeg')
img2 = cv2.imread('real92.jpeg')
img3 = cv2.imread('real3.jpeg')
img4 = cv2.imread('real9.jpeg')
img5 = cv2.imread('real12.jpeg')
img6 = cv2.imread('real92.jpeg')




# cv2.putText(img , Number , (10, 200) , cv2.FONT_HERSHEY_SIMPLEX , 1.5 , (0 , 0, 255) , 3)


images = [img ,img1 , img2 , img3 , img4 , img5 ]

num = []

for i in range(len(images)):
    num.append(numberdet(images[i]))

for i in range(len(images)):
    images[i] = cv2.cvtColor(images[i] , cv2.COLOR_BGR2RGB)

for i in range(len(images)):
    plt.subplot(2 ,3 ,i+1 ) , plt.imshow(images[i] , 'gray')
    plt.title(num[i])
    plt.xticks([]) , plt.yticks([])

plt.show()
#cv2.imshow('image' ,mask2)
# cv2.imshow('image2' ,img)

# cv2.imshow('mask' ,mask)
# cv2.imshow('mask1' ,mask1)


cv2.waitKey(0)
cv2.destroyAllWindows()