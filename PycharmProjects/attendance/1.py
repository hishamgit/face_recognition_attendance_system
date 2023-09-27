import pyforest
import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)  # zero for webcam

abu_image = face_recognition.load_image_file("photos/abu.jpg")
abu_encoding = face_recognition.face_encodings(abu_image)[0]

manu_image = face_recognition.load_image_file("photos/manu.jpg")
manu_encoding = face_recognition.face_encodings(manu_image)[0]

rocky_image = face_recognition.load_image_file("photos/rocky.jpg")
rocky_encoding = face_recognition.face_encodings(rocky_image)[0]

damu_image = face_recognition.load_image_file("photos/damu.jpg")
damu_encoding = face_recognition.face_encodings(damu_image)[0]

known_face_encoding = [abu_encoding, manu_encoding, rocky_encoding, damu_encoding]
known_face_names = ["abu", "manu", "rocky", "damu"]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y/%m/%d")

f = open(current_date + '.csv', 'w+', newline='')
lnwriter = csv.writer(f)
while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                name=known_face_names[best_match_index]
            face_names.append(name)
            
