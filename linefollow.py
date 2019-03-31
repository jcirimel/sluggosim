import cv2
import imutils
import numpy as np
import pygame
from pygame.locals import *

class linefollow:
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    location               = (10,25)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    def follow(image, controller, autonomousMode):
        if(autonomousMode):

            # Capture the frames
            #ret, frame = video_capture.read()
            frame = image;

            # Crop the image
            crop_img = frame[266:533, 300:600]
            #crop_img = image;
            # Convert to grayscale
            gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            #red = cv2.cvtColor(crop_img, COLOR_BGR2HSV);
            # Gaussian blur
            blur = cv2.GaussianBlur(gray,(5,5),0)
            # Color thresholding
            ret,thresh1 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

            # Erode and dilate to remove accidental line detections
            mask = cv2.erode(thresh1, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)

            mask = cv2.bitwise_not(mask);

            # Find the contours of the frame
            contours,hierarchy = cv2.findContours(mask.copy(), 1, cv2.CHAIN_APPROX_NONE)

            # Find the biggest contour (if detected)
            if len(contours) > 0:
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)

                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])

                cv2.line(crop_img,(cx,0),(cx,600),(255,0,0),1)
                cv2.line(crop_img,(0,cy),(800,cy),(255,0,0),1)
                cv2.drawContours(crop_img, contours, -1, (0,255,0), 1)
                print(cx, cy)

                if cx >= 533:
                    #GPIO.output("P8_10", GPIO.HIGH)
                    #GPIO.output("P9_11", GPIO.LOW)
                    controller.roll_left()
                    #controller.move_up()

                if cx < 533 and cx > 220:
                    #GPIO.output("P8_10", GPIO.LOW)
                    #GPIO.output("P9_11", GPIO.LOW)
                    #controller.stop()
                    i = 0;
                if cx <= 220:
                    controller.roll_right()
                    #controller.move_up()

                else:
                    controller.move_up()

                    #Display the resulting frame
                cv2.imshow('frame',crop_img)
                    #if cv2.waitKey(1) & 0xFF == ord('q'):
                    #    continue
                return

    def run(image, controller, autonomousMode):


        #image is already in working opencv format from an RGB numpy array which is actually BGR in opencv
        controller.stop() #reset controller values; start every run call with this
        #controller.move_in() #exmaple move command

        #example draw text
        cv2.putText(image,'OpenCV Slug',
        linefollow.location,
        linefollow.font,
        linefollow.fontScale,
        linefollow.fontColor,
        linefollow.lineType)

        lower_red = np.array([225,0,0])
        upper_red = np.array([255,255,180])

        lower_blue = np.array([0,0,0])
        upper_blue = np.array([0,0,255])



        mask_blue = cv2.inRange(image, lower_red, upper_red)

        mask_red = cv2.inRange(image, lower_blue, upper_blue)

        blue = cv2.bitwise_and(image,image, mask= mask_blue)

        red = cv2.bitwise_and(image,image, mask = mask_red)

        output = cv2.bitwise_or(blue,red)

        if(autonomousMode):
            linefollow.follow(output, controller, autonomousMode)

        #drawscreen
        #cv2.imshow("OpenCV display",image)
        cv2.waitKey(1)


        return
