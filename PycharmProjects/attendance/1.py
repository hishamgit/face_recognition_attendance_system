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
lnwriter=csv.writer(f)
