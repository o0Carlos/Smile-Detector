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

    # Show the current frame from the webcam
    cv2.imshow('Smile Detector', frame)

    # Display every 1 milisecond if not key pressed 
    cv2.waitKey(1)


# Cleanup (for releasing memory and let other apps use the webcam)
webcam.release()
cv2.destroyAllWindows()