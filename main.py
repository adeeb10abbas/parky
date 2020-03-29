
if __name__ == "__main__":
    import cv2 
    import time  
    live = cv2.VideoCapture('video.avi') 
    car_cascade = cv2.CascadeClassifier('cars.xml') 
    while True: 
        # cam = cv2.VideoCapture(0)
        # ret, image = cam.read()
        #The above code should be uncommented when using
        #when taking in the live feed
        ret, frames = live.read() 
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
        cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
        print(cars) # gives out a list in terms of ((x, y), x+w, y+h)
        # so have 3 points of a rectangle
        if cv2.waitKey(33) == 27: 
            break

    	#need to focus on a ROI so that we can 
	#https://www.learnopencv.com/how-to-select-a-bounding-box-roi-in-opencv-cpp-python/
	#https://stackoverflow.com/questions/46447073/how-to-ignore-part-of-a-image-during-feature-extraction-in-opencv
	#The problem is that we are using python in a bas situation we can be affecting the performance by about 4%!
	# that might be a lot and we should work on it since we should make it as efficient as possible. 

