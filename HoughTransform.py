import numpy as np
import cv2
 
img = cv2.imread('img.format')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
#Use canny edges to detect the right number of straight lines.
edges = cv2.Canny(gray, 300, 500, None, 3)
cv2.imshow('Edge', edges)
 
lines = cv2.HoughLines(edges, 1, np.pi/180, 170, None, 0,0)
#The number of straight lines represented varies depending on the threshold.
 
for i in range(0, len(lines)):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
 
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
 
cv2.imshow('res', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows();
