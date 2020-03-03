# Read all the images and save the path in the filepaths.txt

import cv2
import ntpath
import os
import re
import sys
from email_notification import mail

# Code for retrieving the parent directory
def get_parent_dir(n=1):
    """ returns the n-th parent dicrectory of the current
    working directory """
    current_path = os.path.dirname(os.path.abspath(__file__))
    for k in range(n):
        current_path = os.path.dirname(current_path)
    return current_path

#print(get_parent_dir(n=1))
# Set up folder names for default values
data_folder = os.path.join(get_parent_dir(n=1), "Data")

image_folder = os.path.join(data_folder, "Source_Images")

image_test_folder = os.path.join(image_folder, "Test_Data")

detection_results_folder = os.path.join(image_folder, "Test_Image_Detection_Results")
#detection_results_folder = os.path.join("./Data/Source_Images/", "Test_Image_Detection_Results/")

print(detection_results_folder)

def extract():
	a = open("filepaths.txt", "w")
	for path, subdirs, files in os.walk(detection_results_folder):
		for filename in files:
		    f = os.path.join(path, filename)
		    a.write(str(f) + os.linesep) 
	a.close()

	with open('filepaths.txt') as f:
		list1 = []
		for line in f:
			a = line.rstrip()
			list1.append(a)

		print(list1[0])
		a = list1[0]
		img_path = str(a)
		mail(img_path)
	f.close()

#extract()

