 
import cv2
import numpy as np

def show_alert_box():
    try:
        # Get integer input from the user
        user_input = int(input("Enter an integer between 1 and 20: "))
        
        # Check if the entered integer is within the specified range
        if 0 <= user_input <= 20:
            # Display the alert box with the entered integer
            alert_text = f"You entered: {user_input}"
            print("Alert:", alert_text)
            return user_input
            
        else:
            print("Invalid input. Please enter an integer between 1 and 20.")
            show_alert_box()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Call the function to show the alert box
inside=show_alert_box()
img_url=["reimagefortesting/IMG-20230331-WA0037.jpg","reimagefortesting/IMG-20230331-WA0038.jpg","reimagefortesting/IMG-20230331-WA0036.jpg"]
img = cv2.imread(img_url[1])
roi = cv2.selectROI('Select ROI', img, fromCenter=False, showCrosshair=False)

# Crop the selected ROI
cropped_roi = img[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]
img=cropped_roi
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(gray, (5, 5), 16) 
count=0
# 21-32
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT, 1, 20, param1 = 130,param2 = 30, minRadius = 8, maxRadius = 32)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        count=count + 1
        cv2.circle(output, (x, y), r, (0, 255, 0), 2)

totalCount=(count*inside)+count 
print(f"outside circle count :{count}")
print(f"inner circle count in each outside circle :{inside}")
print(f"total circle count :{totalCount}")


cv2.imshow(f'outer circle Detected image-',output)
cv2.waitKey(0)
print("code completed")