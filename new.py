import cv2
import numpy as np
import os
from train import train
from face_detect import *
import sqlite3


def add_to_database(name, faces_path):

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("SELECT MAX(Id) FROM data")
    ma = cur.fetchall()[0][0]
    if ma==None:
        ma=0
    id = str(ma + 1)

    faces = face_detect(faces_path)
    labels = [ma+1]*len(faces)
    train(faces, labels)
    cur.execute("INSERT INTO data VALUES(?, ?)", (id, name))
    conn.commit()
    cur.close()
    conn.close()








