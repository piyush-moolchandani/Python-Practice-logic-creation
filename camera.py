import cv2
import winsound
import time

# Human detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Webcam
cap = cv2.VideoCapture(0)

# Video writer settings
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False

last_seen = 0
last_capture = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect humans
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))

    person_detected = len(boxes) > 0

    if person_detected:

        last_seen = time.time()

        # Alarm sound
        winsound.Beep(1200, 200)

        # Save photo every 4 seconds
        if time.time() - last_capture > 4:
            filename = f"intruder_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            print("Saved:", filename)
            last_capture = time.time()

        # Start recording if not already
        if not recording:
            video_name = f"intruder_video_{int(time.time())}.avi"
            out = cv2.VideoWriter(video_name, fourcc, 20.0,
                                  (frame.shape[1], frame.shape[0]))
            recording = True
            print("Recording started:", video_name)

    # Stop recording if person gone for 5 sec
    if recording and time.time() - last_seen > 5:
        out.release()
        recording = False
        print("Recording stopped")

    # Write video frames
    if recording:
        out.write(frame)

    # Draw detection boxes
    for (x,y,w,h) in boxes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,"HUMAN DETECTED",
                    (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,(0,0,255),2)

    cv2.imshow("Smart AI CCTV", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()

if out:
    out.release()

cv2.destroyAllWindows()

def night_vision(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)

    night = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

    return night


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    night_frame = night_vision(frame)

    cv2.imshow("Normal Camera", frame)
    cv2.imshow("Night Vision", night_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()