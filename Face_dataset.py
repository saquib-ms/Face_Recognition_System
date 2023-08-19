import cv2
import os

cam = cv2.VideoCapture(0)    
cam.set(3, 640)  
cam.set(4, 480) 

if not cam.isOpened():
    print("Error: Could not open webcam.")
    exit()

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("Enter User ID: ")

print("\n [INFO] Initializing face capture")
count = 0
while (True):
    ret, img = cam.read()
    
    if not ret:
        print("Error: Failed to capture frame from webcam")
        break
    
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", grey[y:y+h, x:x+w])
        cv2.imshow('image', img)
        k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:
        break

print("\n [INFO] Exiting Program")
cam.release()
cv2.destroyAllWindows()


