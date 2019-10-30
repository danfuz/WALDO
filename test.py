import numpy
import cv2
result = cv2.matchTemplate(cv2.imread("./whereIs/where.jpg"), cv2.imread("./Faces/face.png"), cv2.TM_CCOEFF_NORMED)
maxx = max(map(max, result))
where = numpy.where(result == maxx)
y = int(where[0])
x = int(where[1])


img = cv2.imread("whereIs/where.jpg")
cv2.rectangle(img, (x-2,y-2),(x+62, y+62),(0,0,0), 3)
cv2.imshow("s", img)
cv2.waitKey(0)

