import numpy
import cv2
import math
import requests

img = cv2.imread("./whereIs/where.jpg")
result = cv2.matchTemplate(img, cv2.imread("./Faces/waldoface.png"), cv2.TM_CCOEFF_NORMED)
maxx = max(map(max, result))
url = "https://www.marxists.org/archive/marx/works/download/pdf/Manifesto.pdf"
response = requests.get(url)
with open('manifesto.pdf', 'wb') as f:
    f.write(response.content)
where = numpy.where(result == maxx)
scale_percent = 101
print (maxx)
i = 0
while maxx < .6:
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    result = cv2.matchTemplate(img, cv2.imread("./Faces/waldoface.png"), cv2.TM_CCOEFF_NORMED)
    maxx = max(map(max, result))
    print(maxx)
    i = i +1

    where = numpy.where(result == maxx)

print(where)
growthP = math.pow(1.01, i)*100
print (growthP)
y = int(where[0]*100/growthP)
x = int(where[1]*100/growthP)

img = cv2.imread("./whereIs/where.jpg")

cv2.rectangle(img, (x-2,y-2),(x+17, y+30),(0,0,0), 3)
cv2.imshow("s",img)
cv2.waitKey(0)

