
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

    
