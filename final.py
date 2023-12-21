import cv2
import numpy as np

img = cv2.imread("reimagefortesting/IMG-20230331-WA0037.jpg")

output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(gray, (5, 5), 16) 
arr=[]
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT, 1, 20, param1 = 130,param2 = 30, minRadius = 21, maxRadius = 32)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        # cv2.circle(output, (x, y), r, (0, 255, 0), 2)
        # Calculate ROI coordinates
        roi_x1, roi_y1 = x - r - 8, y - r - 8
        roi_x2, roi_y2 = x + r + 8, y + r + 8

        if (roi_x1 >= 0 and roi_y1 >= 0 and roi_x2 < output.shape[1] and roi_y2 < output.shape[0]):
            arr.append([roi_x1,roi_y1,roi_x2,roi_y2])
            single_roi = output[roi_y1:roi_y2, roi_x1:roi_x2]
        
i=1

ot=output[arr[i][1]:arr[i][3], arr[i][0]:arr[i][2]]

gx = cv2.cvtColor(output[arr[i][1]:arr[i][3], arr[i][0]:arr[i][2]], cv2.COLOR_BGR2GRAY)
  
    
circlexs = cv2.HoughCircles(gx,cv2.HOUGH_GRADIENT, 1, 20, param1 = 15,param2 = 30, minRadius = 30, maxRadius = 32)

if circlexs is not None:
    circlexs = np.round(circlexs[0, :]).astype("int")
    for (x, y, r) in circlexs:
        cv2.circle(ot, (x, y), r, (0, 255, 0), 1)

   
circlexs = cv2.HoughCircles(gx,cv2.HOUGH_GRADIENT, 1, 20, param1 = 15,param2 = 30, minRadius = 24, maxRadius = 36)

if circlexs is not None:
    circlexs = np.round(circlexs[0, :]).astype("int")
    for (x, y, r) in circlexs:
        cv2.circle(ot, (x, y), r, (255, 255, 0), 1)
                
 
circlexs = cv2.HoughCircles(gx,cv2.HOUGH_GRADIENT, 1, 20, param1 = 15,param2 = 30, minRadius = 22, maxRadius = 23)

if circlexs is not None:
    circlexs = np.round(circlexs[0, :]).astype("int")
    for (x, y, r) in circlexs:
        cv2.circle(ot, (x, y), r, (0, 0, 255), 1)
        

 
circlexs = cv2.HoughCircles(gx,cv2.HOUGH_GRADIENT, 1, 20, param1 = 15,param2 = 30, minRadius = 16, maxRadius = 19)

if circlexs is not None:
    circlexs = np.round(circlexs[0, :]).astype("int")
    for (x, y, r) in circlexs:
        cv2.circle(ot, (x, y), r, (255, 0, 0), 1)


cv2.imshow(f'outer circle Detected image-{i}',ot)

    
cv2.waitKey(0)
print("code completed")
