#client_init.py
#Python 2
#Client script - connects to server, uses built-in webcam to capture image.
#	Triggered using motion based on changes in the image.


#imports
from cv2 import *
from Tkinter import *
import datetime
import time


#global vars
log_name = ""
var1 = ""
server_Name = ""
server_Token = ""


def init_log():
	#initilizes log file
	date = datetime.date.today().strftime("%Y-%b-%dT%I_%m_%S")
	global log_name
	log_name = "client_secureCam_log_" + date + ".txt"
	log_file = open(log_name,'w') #creates log

def write_to_log(log):
	#writes string to log
	print log
	log_file = open(log_name, 'a')
	log_file.write(log)
	log_file.close()

def image_capture(cam):
	#Captures image
	s,img = cam.read()
	if s:
		imwrite("filename.jpg",img)
		return img
	return False

def image_motion_detect(img1,img2):
	#Processes image
	frameDelta = cv2.absdiff(img1, img2)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)



def server_connect():
	#Get server credentials and connect

	write_to_log("Asking for server credentials.")
	global server_Name
	global server_Token
	server_Name = raw_input("Enter Server Name: ")
	server_Token = raw_input("Enter Server Token: ")

	return server_Name, server_Token

def server_image_upload(fileToUpload):
	#Saves file locally and uploads to google drive
	#liam 
	print "TODO"

def main():
	#main
	init_log()
	write_to_log("Client Starting...")
	#server_connect()

	#Get initial frames
	cam = VideoCapture(0)
	prev_image = image_capture(cam)
	time.sleep(1)
	curr_image = image_capture(cam)
	image_motion_detect(prev_image,curr_image)
	#compare prev and curr for motion detection
	
	
	#while no detection
		#get new image and delay a few seconds
		#if motion detection save previous and current and start video recording for a set time
		#after done recording start cycle again and wait for motion
		#when motion occurs save it to
	#while():

	#	prev_image = curr_image
	#	curr_image = image_capture()

	
	write_to_log("Disconnecting Camera.")
	cam.release()
	write_to_log("End of Processing")


main()
