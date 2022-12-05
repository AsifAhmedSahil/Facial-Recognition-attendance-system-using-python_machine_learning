import face_recognition;
import cv2;
import numpy as np;
import csv;

import os;
from datetime import datetime;

video_capture = cv2.VideoCapture(0)

elon_image =face_recognition.load_image_file("photos/elon (1).jpg")
elon_encoding = face_recognition.face_encoding(elon_image)[0]

tesla_image =face_recognition.load_image_file("photos/tesla.jpg")
tesla_encoding = face_recognition.face_encoding(tesla_image)[0]

known_face_encoding = [
    elon_encoding,
    tesla_encoding
]

known_face_names = [
    "elon",
    "tesla"
]

students = known_face_names.copy()

face_location = []
face_encoding = []
face_names = []
s=True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f  = open(current_date+".csv","w+",newline= "")
lnwrite = csv.writer(f)

while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_location = face_recognition.face_locations(rgb_small_frame)
        face_encoding = face_recognition.face_encoding(rgb_small_frame,face_location)
        face_names = []
        for face_encoding in face_encoding:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name =""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                
            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwrite.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
        
    
                



