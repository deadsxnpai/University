import cv2 

path_to_img = '/home/deadsxnpai/Downloads/University/Diploma/code/learn_img/daniil.jpg'

img = cv2.imread(path_to_img)

face_recog = cv2.CascadeClassifier('/home/deadsxnpai/Downloads/University/Diploma/code/code/haarcascade_frontalface_alt.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_result = face_recog.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4) 
if len(face_result) != 0:
	for index, (x,y,w,h) in enumerate(face_result):
		img = img[x:y+h]
    
		cv2.imwrite(f'Diploma/code/images/{index}.jpg', img)
cv2.imshow("Result", img)