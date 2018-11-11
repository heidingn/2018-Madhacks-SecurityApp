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
	log_name = "client_secureCam_log_" + date
	log_file = open(log_name,'w') #creates log

def write_to_log(log):
	#writes string to log
	print log
	log_file = open(log_name, 'w')
	log_file.write(log)
	log_file.close()

def image_capture():
	#Captures image
	cam = VideoCapture(0)
	s,img = cam.read()
	if s:
		namedWindow("cam-test")
		imwrite("filename.jpg",img)

def image_processing():
	#Processes image
	print "TODO"

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
	

	server_connect()
	image_capture()

	

	write_to_log("End of Processing")


main()
