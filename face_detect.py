import cv2
import os
import numpy as np

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_detect_single(image):

    face = detector.detectMultiScale(
        image,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if len(face) != 1:
        return ([],[],[],[]), []

    for (x, y, w, h) in face:
        return (x, y, w, h), image[y:y + h, x:x + w]

def face_detect(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []

    for image in imagePaths:
        Image = cv2.imread(image, 0)
        Image = np.array(Image)

        face = detector.detectMultiScale(
            Image,
            scaleFactor=1.15,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        if len(face) != 1:
            continue

        for (x, y, w, h) in face:
            faces.append(Image[y:y + h, x:x + w])

    return faces
