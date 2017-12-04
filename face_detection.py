"""
Takes pictures from the Raspberry Pi Camera at regular intervals. Detects faces
and sends cropped pictures of faces to the server
"""

import cv2
import requests


SERVER_URL = 'http://127.0.0.1:5000/image'


cascPath = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)


with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.capture('photo.jpg', format='jpeg')


img = cv2.imread('photo.jpg', 0)

faces = faceCascade.detectMultiScale(
    img,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Send each face to the server
for (x, y, w, h) in faces:
    cv2.imwrite('cropped.jpg', img[y:y + h, x:x + w])

    # Send the image using the requests library
    files = {'file': open('cropped.jpg', 'rb')}

    requests.post(SERVER_URL, files=files)
