class algo:
    def run(image, controller):
        #image is already in working opencv format from an RGB numpy array which is actually BGR in opencv 
        controller.stop() #reset controller values; start every run call with this
        controller.move_in() #exmaple move command
        
        return 

