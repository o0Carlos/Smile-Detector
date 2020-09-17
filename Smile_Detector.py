import cv2

# Face classifier

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Wil return if we are smiling or no. 

webcam = cv2.VideoCapture(0) # 0 for webcam

#how he current frame

while True:

    successful_frame_read, frame = webcam.read() #Reads single frame

    # Abort process when there's an error
    if not successful_frame_read:
        break

    # Change to grayscale (look at Haar Cascade of why we use this)
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces [return a list of points]
    faces = face_detector.detectMultiScale(frame_grayscale)
    
    # Run smile detection in those faces
    for(x, y, w, h) in faces:
        # Draw a rectangle around the face in the COLOR FRAME. (the numbers
        # are the color code and the 4 means the border thickness)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

    # Show the current frame from the webcam
    cv2.imshow('Smile Detector', frame)


    # Display every 1 milisecond if not key pressed 
    cv2.waitKey(1)


# Cleanup (for releasing memory and let other apps use the webcam)
webcam.release()
cv2.destroyAllWindows()