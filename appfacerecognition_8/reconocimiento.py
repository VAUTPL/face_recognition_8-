##########################################################################################
#					  UNIVERSIDAD TECNICA PARTICULAR DE LOJA         #
#....................................................................................... #
#DEVELOPMENT OF AN APPLICATION FOR FACIAL RECOGNITION USING THE ALGORITHM FISHERFACES	 #
#																						 #
#Authors: Carlos Saca (cfsaca@utpl.edu.ec), Critian Ortiz (ceortiz2@utpl.edu.ec)         #
#Professor: Ing. Luis Rodrigo Barba							 #
#Date: 16/01/2017									 #
#........................................................................................#
#System Requirements:									 #
#Ubuntu: 16.4										 #
#Python: 2.7+										 #
#OpenCv: 3.0.0										 #
##########################################################################################
import os
import numpy as np
import cv2, sys
size = 2
fn_haar = 'haarcascade_frontalface_alt.xml'
fn_dir = 'rostros'
#Creando fisherRecognizer
print('Formando...')
# Create a list of images and a list of corresponding names
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(fn_dir):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(fn_dir, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)
# Create a Numpy array from the two previous lists
(images, lables)=[np.array(lis) for lis in [images, lables]]
# OpenCV trains a model from the images
model=cv2.face.createFisherFaceRecognizer()
model.train(images, lables)
# Use fisherRecognizer to operate the camera
haar_cascade = cv2.CascadeClassifier(fn_haar)
webcam = cv2.VideoCapture(0)
while True:
    (rval, frame) = webcam.read()
    frame=cv2.flip(frame,1,0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mini = cv2.resize(gray, (gray.shape[1] / size, gray.shape[0] / size))
    faces = haar_cascade.detectMultiScale(mini)
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))
        # Tried to recognize the face
        prediction = model.predict(face_resize)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # Writing the name of the face recognized        
        if prediction[1]<150:
	  cv2.putText(frame,
          '%s - %.0f' % (names[prediction[0]],prediction[1]),
          (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
   	  #The face variable will have the name of the recognized person  
   	  cara = '%s' % (names[prediction[0]])    	
 	 #If the face is unknown, put unknown
	else:
	  cv2.putText(frame,
	    'Desconocido',
	    (x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))	  	       	
    cv2.imshow('OpenCV', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
