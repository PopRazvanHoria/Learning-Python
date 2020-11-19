import numpy as np
import cv2

image = cv2.imread('images\img.png')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


#Red color rangle  169, 100, 100 , 189, 255, 255


lower_range = np.array([169,100,100])
upper_range = np.array([189,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

output = image.copy()


# detect circles in the image
circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 3, 50)
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

# cv2.destroyAllWindows()
cv2.destroyAllWindows()