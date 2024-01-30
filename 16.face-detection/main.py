import cv2

face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier()
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    print("Error loading xml file")
    exit(0)

img = cv2.imread("test.jpg")

if img is None:
    print("Error loading image")
    exit(0)
    
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

cv2.imshow("img", img)

cv2.waitKey(0)

cv2.imwrite("face_detected.jpg", img)
