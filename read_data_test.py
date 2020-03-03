# Read all the images and save the path in the filepaths.txt

import cv2
import ntpath
import os
import re
import sys
from email_notification import mail
import numpy as np
import pandas as pd

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
def email_result():
	data_folder = os.path.join(get_parent_dir(n=1), "Data")

	image_folder = os.path.join(data_folder, "Source_Images")

	#image_test_folder = os.path.join(image_folder, "Test_Data")
	image_test_folder = "./img/"

	#detection_results_folder = os.path.join(image_folder, "Test_Image_Detection_Results")
	detection_results_folder = './Test_Image_Detection_Results/'

	#detection_results_file = os.path.join(detection_results_folder, "Detection_Results.csv")
	detection_results_file = "./Test_Image_Detection_Results/Detection_Results.csv"

	df = pd.read_csv(detection_results_folder + 'Detection_Results.csv')
	#print(df)
	df1 = df[df['label'] == 2]
	#print(df1.image_path)
	#a = df1.image_path
	b = "abc"
	for a in df1.image_path:
		#print(type(a))	
		temp = a[6:]
		#updated_path = os.path.join(detection_results_folder , temp)
		updated_path = detection_results_folder + temp
		print(updated_path)
		#b = a[0]
		#print(b)
		if b != a:								# Handle multiple image issues
			mail(updated_path)
		b = a

# email_result()
# print(df1.item)
# list = []
# list = list.append(b)
# print(list)
# if df1.item == 2:
# 	print(df.image_path)