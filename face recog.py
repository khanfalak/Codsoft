import cv2

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('E:\\FALAK\\facerecog\\haarcascade_frontalface_default.xml')

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Flag to indicate if a face has been detected in the current frame
face_detected = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if not face_detected:
            # Capture and save the detected face
            face = frame[y:y+h, x:x+w]
            img_name = "detected_face.jpg"
            cv2.imwrite(img_name, face)
            face_detected = True

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
