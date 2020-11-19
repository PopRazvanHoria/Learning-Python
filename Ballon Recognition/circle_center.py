# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.5, 50)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	cv2.imshow("output", np.hstack([image, output]))
	cv2.waitKey(0)
else:
	print("there is no circle")

# img = cv2.imread('img.png')

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# #Red color rangle  169, 100, 100 , 189, 255, 255


# lower_range = np.array([110,50,50])
# upper_range = np.array([130,255,255])

# mask = cv2.inRange(hsv, lower_range, upper_range)

# cv2.imshow('image', img)
# cv2.imshow('mask', mask)


# cv2.waitKey(0)
# cv2.destroyAllWindows()