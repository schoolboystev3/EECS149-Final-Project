# USAGE
# python barcode_scanner_image.py --image barcode_example.png

# import the necessary packages
from pyzbar import pyzbar
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())

def computeCenter(list):
        x = 0
        y = 0
        for point in list:
                x += point[0]
                y += point[1]
        return (x / 4, y / 4)

# load the input image
img = cv2.imread(args["image"])

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# find the barcodes in the image and decode each of the barcodes
barcodes = pyzbar.decode(gray)

file = open("test_sim_pos.txt", "w")

# loop over the detected barcodes
for barcode in barcodes:
	# extract the bounding box location of the barcode and draw the
	# bounding box surrounding the barcode on the image
	(x, y, w, h) = barcode.rect
	cv2.rectangle(resized, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# the barcode data is a bytes object so if we want to draw it on
	# our output image we need to convert it to a string first
	barcodeData = barcode.data.decode("utf-8")
	barcodeType = barcode.type

	# draw the barcode data and barcode type on the image
	text = "{} ({})".format(barcodeData, barcodeType)
	cv2.putText(resized, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.5, (0, 0, 255), 2)

        # compute center of adversary, crazyflie
	if (barcodeData == "adversary"):
		#print("We see you, adversary o.o")
		advPos = computeCenter(barcode.polygon)
	if (barcodeData == "crazyflie"):
		#print("Hello, crazyflie!")
		crazyfliePos = computeCenter(barcode.polygon)

if (advPos and crazyfliePos):
	file.write(str(advPos[0]))
	file.write(" ")
	file.write(str(603.0 - advPos[1]))
	file.write(" ")
	file.write(str(crazyfliePos[0]))
	file.write(" ")
	file.write(str(603.0 - crazyfliePos[1]))
else:
	file.write("0 0 0 0")
file.flush()
file.close()


# show the output image
cv2.imshow("Image", resized)
cv2.waitKey(0)
