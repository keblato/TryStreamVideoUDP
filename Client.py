
#!/bin/env python3
#-*- encoding: utf-8 -*-

import cv2
import numpy as np

# start this:
# ffmpeg -i /dev/video0 -f mpegts udp://localhost:1337
# ffmpeg -i rtsp://... -f mpegts udp://localhost:1337
print("Que canal desea reproducir?")
print("-----------1. Video de Zeus")
print("-----------2. Video de Rambo")
print("-----------3. Noticias")

input1 = input() 
#-----------Cambiar la ip 
ip = "udp://192.168.1.18:"
if input1 == "1":
    ip = ip + "1337"
elif input1 == "2":
    ip = ip + "1338"
else:
    ip = ip + "1339"

cameraCapture = cv2.VideoCapture(ip)
cv2.namedWindow('MyWindow')

print('Click window or press any key to stop.')

while True:
    success, frame = cameraCapture.read()
    cv2.imshow('MyWindow', frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cv2.destroyWindow('MyWindow')
cameraCapture.release()

""" import numpy as np
import cv2

cap = cv2.VideoCapture()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows() """

""" 
import numpy as np
import cv2

cap = cv2.VideoCapture('F:/ARCHIVOS/Documentos/GitHub/APRENDIENDO/Python/UDP/vtest.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() """