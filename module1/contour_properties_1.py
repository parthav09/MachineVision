import cv2
from argparse import ArgumentParser
import imutils

ap = ArgumentParser()
ap.add_argument("-i", "--image", help = "Path to the image is required", required =True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
clone = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
    M = cv2.moments(c)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    cv2.circle(clone, (cx, cy), 10, (0, 255, 0), -1)
cv2.imshow("Centroids", clone)

#calculating the area and the perimeter
for (i, c) in enumerate(cnts):
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print("Contour: {a} --area: {b} --perimeter: {c}".format(a=i, b=area, c=perimeter))
    cv2.drawContours(clone, c, -1, (0, 255, 0), 2)
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.putText(clone, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,1.25, (255, 255, 255), 4)
cv2.imshow("Contours", clone)

cv2.imshow("Original: ", image)
cv2.waitKey()