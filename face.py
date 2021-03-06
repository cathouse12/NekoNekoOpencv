from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import serial

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects
    

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


# initialize the camera and grab a reference to the raw camera capture

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalcatface.xml")
# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    img = frame.array
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    rects = detect(gray, cascade)
    vis = img.copy()
    draw_rects(vis, rects, (0, 255, 0))

    # 프레임 출력
    cv2.imshow("Frame", vis)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):

        break
	
	if faces.size() > 0:
		
	ser = serial.Serial('COM1', 9600)
	print(ser)
	ser.write('1')
		
		#detectStatus = '1'
		#if (temp == '0') {
			#print('detect!')
			#serialComm.sendCommand('1')
			#temp = '1'
			
	else:
	
	ser = serial.Serial('COM', 9600)
	print(ser)
	ser.write('1')
	
		#detectStatus = '0'
		#if (temp == '1') 
			#print('unknown')
			#serialComm.sendCommand('0')
			#temp = '0'
	
