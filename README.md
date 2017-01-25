# face_recognition_8-
##Develop an application for face recognition using fisherfaces algoritm
#UTPL 
#Professor: Rodrigo Barba lrbarba@utpl.edu.ec 
#Students: 
###Cristian Ortiz Celi ceortiz2@utpl.edu.ec 
###Carlos Saca Japa cfsaca@utpl.edu.ec 
#FACIAL RECOGNITION APLICATION WHIT FISHERFACES ALGORITM  
This work is done in order to put practical knowledge of machine vision using OpenCV and Pyhton, it can be edited and modified by anyone interested in improving it. It was designed with the purpose of recognizing faces that previously program the stores in a database to then make the comparison and present a result in real time 

#System Requirements 
#####An i3 or better processor. The faster the better, especially at high video resolutions. 
#####2 GB or more RAM memory. 
#####At least 100 MB Free Disk space  
#####Ubuntu 16.04  
#####Python 2.7+ Open CV 3.0.0 
#####Web cam. 

#Installation on Ubuntu 16.04 1.  
First, one should install the following libraries:  
#####OpenCV version 3.0 
#####Python 2.7+  
#####libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev 
#####libgtk2.0-dev 
#####libavcodec-dev libavformat-dev libswscale-dev libv4l-dev 
#####libatlas-base-dev gfortran 
#####Install pip 
#####Install virtualenv and virtualenvwrapper  

2.  Now download and extract this repository with one of several options: 
◦ Clone the repository with $ git clone https://github.com/VAUTPL/Deteccion.git 
◦ Download the repository as a .zip or .tar.gz and then extract it. 

#Running
To run the application, follow these instructions: 

By means of the terminal we raise the virtual environment with the command 

###$ mkvirtualenv cv

We execute the training to include faces to the database with the command 

###$ python capture.py &lt;Name of the person> 

we must be inside the directory where we have the necessary files for the application

To start the reconnaissance, we execute the command 

###$ python  reconocimiento.py
