import cv2


#Trained face data
trained_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img
# img=cv2.imread('padam.jpeg')

webcam=cv2.VideoCapture(0)
webcam.set(3,500)
webcam.set(4,500)
while True:
    success,frame=webcam.read()
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinates = trained_face.detectMultiScale(imgGray)
    for (x, y, w, h) in face_cordinates:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 2)

    cv2.imshow("Output Webcam",frame)
    key=cv2.waitKey(1)

    if key == 81 or key == 113:
        break





