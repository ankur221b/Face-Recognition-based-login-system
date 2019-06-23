import cv2
from face_detect import *
import time
import sqlite3
import os


global name

def get_name(id):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM data WHERE Id=? ", (id,))
 
    name = cur.fetchall()[0][1]

    return name


def recognize(img):

    if os.path.isfile('./recognizer.yml') == False:
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.save('recognizer.yml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer.yml')
    
    Id, confidence = recognizer.predict(img)

    return Id, confidence


def login():

    st = time.time()

    cap = cv2.VideoCapture(0)

    count = 0

    while True:

        count += 1
        print(count)

        is_pic, frame = cap.read()

        if count <= 10:
            continue

        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        (x, y, w, h), img = face_detect_single(img)

        if img == []:
            continue

        a, b = recognize(img)

        if a != -1:
            name = get_name(str(a))
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count == 500:
            break

    cap.release()
    cv2.destroyAllWindows()
    return str(name)
