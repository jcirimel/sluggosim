import cv2
import numpy as np
class algo:
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    location               = (10,25)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    def run(image, controller):
 
        #image is already in working opencv format from an RGB numpy array which is actually BGR in opencv 
#        controller.stop() #reset controller values; start every run call with this
 #       controller.move_in() #exmaple move command

        #example draw text
        cv2.putText(image,'OpenCV Slug', 
        algo.location, 
        algo.font, 
        algo.fontScale,
        algo.fontColor,
        algo.lineType)        
        
        crack_width = 1.85

        #drawscreen
        lower_red = np.array([225,0,0])
        upper_red = np.array([255,255,180])

        lower_blue = np.array([0,0,0])
        upper_blue = np.array([0,0,255])

        

        mask_blue = cv2.inRange(image, lower_red, upper_red)

        mask_red = cv2.inRange(image, lower_blue, upper_blue)
            
        blue = cv2.bitwise_and(image,image, mask= mask_blue)

        red = cv2.bitwise_and(image,image, mask = mask_red)

        output = cv2.bitwise_or(blue,red)


        
        CANNY = 250
        MORPH = 7


       
        #dimensions of rect
        _width  = 600.0
        _height = 420.0
        _margin = 0.0

        #dimensions of rect 
        corners = np.array(
                [
                        [[ _margin, _margin ]],
                        [[ 	_margin, _height + _margin]],
                        [[ _width + _margin, _height + _margin]],
                        [[ _width + _margin, _margin]],
                ]

        )

        pts_dst = np.array( corners, np.float32 )

        def adjust_gamma():
            print("TBD")

               
        def findRect(colorMask, COLOR, colorString):
            colorMask = cv2.bilateralFilter(colorMask,1,10,120)
            edges = cv2.Canny(colorMask,10,CANNY)
            kernelShape = cv2.getStructuringElement( cv2.MORPH_RECT, ( MORPH, MORPH ) )
            closed = cv2.morphologyEx( edges, cv2.MORPH_CLOSE, kernelShape ) #fill in noisy spots

            cv2.imshow(colorString+ ' rect edges',edges)
            _, contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
            
            for cont in contours:
                area = cv2.contourArea(cont)
                if area > 200: #maybe change the area here
                    arc_len = cv2.arcLength(cont, True)
                    approx = cv2.approxPolyDP(cont, 0.1 * arc_len, True)
                    
                    #c = max(cont, key=cv2.contourArea) #find the max contour 

                    if(len(approx) ==4):
                        #THIS SHIT DOES NOT WORK YET 
                        (x,y,w,h) = cv2.boundingRect(approx)
                        print("found " + colorString + " rectangle")
                        pts_src = np.array( approx, np.float32 )
                        h, status = cv2.findHomography( pts_src, pts_dst )
                        out = cv2.warpPerspective( colorMask, h, ( int( _width + _margin * 2 ), int( _height + _margin * 2 ) ) )
                        cv2.drawContours( frame, [approx], -1, ( 0, 0, 0 ), 2 )
                        cv2.putText(frame, colorString + ' square',(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, COLOR)

                    else:
                        pass 
        while True:
           
            # Convert RGB to HSV
            hsv = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
            BLUE = (255, 0, 0)
            #gotta make a black mask for finding Numbers
       #                pass
            findRect(blue, BLUE, "blue")

            #findShapes(maskBlue, "blue", 4, "square")
            

                
            #Make frame tracking object
                
            #Display live video frame
            cv2.imshow('blue mask',blue)
            
        #    if isSquares:
        #        cv2.imshow('output Squares', out)
                
            # Write frame to file
            #frame = cv2.flip(frame,0)
            
            #Press ESC to exit 

        
        cv2.imshow("OpenCV display",output)
        #cv2.imshow("OpenCV display red",red)
        cv2.waitKey(1)
        return 

