import cv2
import numpy as np
import os

def init():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.save('recognizer.yml')


def train(faces, labels):
    if os.path.isfile('./recognizer.yml') == False:
        init()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('recognizer.yml')
    recognizer.update(faces, np.array(labels))
    recognizer.save('recognizer.yml')



