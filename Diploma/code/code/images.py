import cv2
import face_recognition


image_to_recognition = face_recognition.load_image_file('/home/deadsxnpai/Downloads/University/Diploma/code/images/0.jpg')
image_enc = face_recognition.face_encodings(image_to_recognition)[0]

# Load the cascade
face_cascade = cv2.CascadeClassifier('/home/deadsxnpai/Downloads/University/Diploma/code/code/haarcascade_frontalface_alt.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # if len(faces) != 0:
    #     print("Лицо нашел")
    #     unknown_face = face_recognition.face_encodings(img)
    #     compare = face_recognition.compare_faces([unknown_face], image_enc)

    #     if compare == True:
    #         print('Equal')
    #     else:
    #         print("Not equal")
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
       cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()