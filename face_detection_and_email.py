import cv2
import os
from extract_and_read import extract

#import the cascade for face detection
FaceClassifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# access the webcam (every webcam) 
capture = cv2.VideoCapture(0)
count = 0 

for filename in os.listdir('./faces/'):
    print(filename)
    if filename.endswith('.jpg'):
        filename = './faces/' + filename
        os.remove(filename)

# os.remove('./faces' + filename) for './faces/'+filename in os.listdir('./faces/') if filename.endswith('.jpg')

while(True):
    # Capture frame-by-frame

    ret, frame = capture.read()
    if not capture:
        print ("Error opening webcam device")
        sys.exit(1)

    # to detect faces in video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = FaceClassifier.detectMultiScale(gray, 1.3, 5)

    # Resize Image 
    minisize = (frame.shape[1],frame.shape[0])
    miniframe = cv2.resize(frame, minisize)
    # Store detected frames in variable name faces
    faces =  FaceClassifier.detectMultiScale(miniframe)
    # Draw rectangle 
    for f in faces:
        x, y, w, h = [ v for v in f ]
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,255,255))
        count += 1
        #Save just the rectangle faces in SubRecFaces
        sub_face = frame[y:y+h, x:x+w]
        FaceFileName = "faces/face_" + str(y) + ".jpg"
        cv2.imwrite(FaceFileName, sub_face)
        #Display the image 
        cv2.imshow('Result',frame)
        #cv2.waitKey(0)

    k = cv2.waitKey(100) & 0xff 		# Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 10: 				# Take 5 face sample and stop video
         break

extract()


'''
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
'''
