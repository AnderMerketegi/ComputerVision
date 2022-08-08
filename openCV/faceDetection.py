# import packages
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 225, 0), 3)

    cv2.imshow("Face Detection", img)
    k = cv2.waitKey(30) # check every 30ms if a key is pressed

    if k == 27: # 27 is ESC in ascii -- press ESC to exit
        break

cap.release()



