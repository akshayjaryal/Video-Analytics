# Python program to illustrate 
# saving an operated video 

# organize imports
import cv2
import math
import os
from datetime import datetime
import numpy as np 


def video_to_frame():
	for filename in os.listdir('./img/'):
	    #print(filename)
	    if filename.endswith('.jpg'):
	    	filename = './img/' + filename
	    	os.remove(filename)

	cap = cv2.VideoCapture('output.avi')
	frameRate = cap.get(5) 						#frame rate
	while(cap.isOpened()):
	    frameId = cap.get(1) 					#current frame number
	    ret, frame = cap.read()
	    if (ret != True):
	    	break
	    if (frameId % math.floor(frameRate) == 0):
	    	filename = "./img/frame_" +  str(int(frameId)) + ".jpg"
	    	cv2.imwrite(filename, frame)

	    key = cv2.waitKey(1)
	    								# press 'q' to exit the window
	    if key == ord('q'):
	    	if status == 1:
	    		time.append(datetime.now())
	    	break

	cap.release()
	cv2.destroyAllWindows()
	print ("Done!")


# This will return video from the first webcam on your computer. 
def main():
	cap = cv2.VideoCapture(0) 

	# Define the codec and create VideoWriter object 
	fourcc = cv2.VideoWriter_fourcc(*'XVID') 
	out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 

	# loop runs if capturing has been initialized. 
	while(True): 
		# reads frames from a camera 
		# ret checks return at each frame 
		ret, frame = cap.read() 

		# Converts to HSV color space, OCV reads colors as BGR 
		# frame is converted to hsv 
		#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
		
		# output the frame 
		out.write(frame) 
		
		# The original input frame is shown in the window 
		cv2.imshow('Original', frame) 

		# The window showing the operated video stream 
		#cv2.imshow('frame', hsv) 

		
		# Wait for 'q' key to stop the program 
		if cv2.waitKey(1) & 0xFF == ord('q'): 
			break

	# Close the window / Release webcam 
	cap.release() 

	# After we release our webcam, we also release the output 
	out.release() 

	# De-allocate any associated memory usage 
	cv2.destroyAllWindows()
	# Function for video to frame converter with the gap of 1 second between frames
	video_to_frame()
	 
	 
if __name__ == "__main__":
	main()

