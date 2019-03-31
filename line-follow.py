import cv2
class line-follow:
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    location               = (10,25)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2

    def run(image, controller):

        #image is already in working opencv format from an RGB numpy array which is actually BGR in opencv
        controller.stop() #reset controller values; start every run call with this
        controller.move_in() #exmaple move command

        #example draw text
        cv2.putText(image,'OpenCV Slug',
        line-follow.location,
        line-follow.font,
        line-follow.fontScale,
        line-follow.fontColor,
        line-follow.lineType)

        #drawscreen
        cv2.imshow("OpenCV display",image)
        cv2.waitKey(1)
        return
