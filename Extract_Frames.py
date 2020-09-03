import cv2
import os

folder_name=input("Enter a folder name to save the frames: ")
try:
	os.mkdir(folder_name)
except:
	print("Folder already exists, will be saved there")




#Creating an instance for which video to extract the frames from. By default set to 0 for webcam. You can specify the video file path name instead.
vid_instance=cv2.VideoCapture(0)
count=0

while True:
	#Capture frame by frame
	ret,frame=vid_instance.read()
	#ret is a boolean value that returns True/False if frame is read correctly or not
	if ret is False:
		break
	#Wr	
	cv2.imwrite(os.path.join(folder_name,"frame_{:0>3d}.jpg".format(count)), frame)
	count+=1

#In live capture press Ctrl-C to exit loop.