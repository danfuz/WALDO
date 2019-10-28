import numpy
import cv2
result = cv2.matchTemplate(cv2.imread("./whereIs/where.jpg"), cv2.imread("./Faces/face.png"), cv2.TM_CCOEFF_NORMED)
print(max(map(max, result)))

box = cv2.rectangle('where', )