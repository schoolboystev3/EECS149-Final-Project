# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

advPos = 0 
crazyfliePos = 0 

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=1).start()
time.sleep(2.0)

def computeCenter(list):
        x = 0
        y = 0
        for point in list:
                x += point[0]
                y += point[1]
        return (x / 4, y / 4)

vector = open("vector.txt", "w")

# loop over the frames from the video stream
while True:
        # grab the frame from the threaded video stream and resize it to
        # have a maximum width of 400 pixels
        frame = vs.read()
        #frame = imutils.resize(frame, width=400)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        vector = open("vector.txt", "w")

        # find the barcodes in the frame and decode each of the barcodes
        barcodes = pyzbar.decode(gray)

        # loop over the detected barcodes
        for barcode in barcodes:
                # extract the bounding box location of the barcode and draw
                # the bounding box surrounding the barcode on the image
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # the barcode data is a bytes object so if we want to draw it
                # on our output image we need to convert it to a string first
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type

                # draw the barcode data and barcode type on the image
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # compute center of adversary, crazyflie
                if (barcodeData == "adversary"):
                        print("We see you, adversary o.o")
                        advPos = computeCenter(barcode.polygon)
                if (barcodeData == "crazyflie"):
                        print("Hello, crazyflie!")
                        crazyfliePos = computeCenter(barcode.polygon)


        if (advPos):
                vector.write(str(advPos[0]))
                vector.write(" ")
                vector.write(str(advPos[1]))
                vector.write(" ")
        else:
                print("No adversary detected!")
        if (crazyfliePos):
                vector.write(str(crazyfliePos[0]))
                vector.write(" ")
                vector.write(str(crazyfliePos[1]))
        else:
                print("No crazyflie detected!")
        vector.flush()	

        # show the output frame
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF
 
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop() 
