import cv2

model = cv2.CascadeClassifier('C:/Users/ADMIN/Downloads/haarcascade_fullbody.xml')

video = cv2.VideoCapture('C:/Users/ADMIN/Downloads/180301_06_B_CityRoam_01.mp4')

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    h,w = frame.shape[:2]
    pedestrians = model.detectMultiScale(frame, 1.1,1)
    
    for (x,y,w,h) in pedestrians:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, 'Person', (x+6,y-6), font, 0.5, (0,255,0), 1)
         
    cv2.imshow('frame', frame)
    key = cv2.waitKey(3)
    if key == 27:
        break

cv2.destroyAllWindows()