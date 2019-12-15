# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2

def computeCenter(list):
	x = 0
	y = 0
	for point in list:
		x += point[0]
		y += point[1]
	return (x / 4, y / 4)	


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-o", "--output", required=False, default="out.txt", help="Name of output file")
args = vars(ap.parse_args())

print("Loading image...")

# load the input image
image = cv2.imread(args["image"])

# SAM ADDED
# make greyscale version of image for better processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far 
out = open(args["output"], "w")
vector = open("vector.txt", "w")

# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(gray)

points = {}

# loop over the detected barcodes
for barcode in barcodes:
	# extract the bounding box location of the barcode and draw the
	# bounding box surrounding the barcode on the image
	(x, y, w, h) = barcode.rect
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# the barcode data is a bytes object so if we want to draw it on
	# our output image we need to convert it to a string first
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type

	# SAM ADDED
	points[barcodeData] = barcode
	#print(barcodeData)
	#print(barcode.rect)
	#points.append(barcodeData)

	# compute center of adversary, crazyflie
	if (barcodeData == "adversary"):
		print(barcode.polygon)
		advPos = computeCenter(barcode.polygon)
	if (barcodeData == "crazyflie"):
		crazyfliePos = computeCenter(barcode.polygon)

	# draw the barcode data and barcode type on the image
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)

# SAM ADDED
for point in points:
	#print(point)
	out.write(point)
	out.flush()

vector.write(str(advPos[0]))
vector.write(" ")
vector.write(str(advPos[1]))
vector.write(" ")
vector.write(str(crazyfliePos[0]))
vector.write(" ")
vector.write(str(crazyfliePos[1]))
vector.flush()

# show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)


