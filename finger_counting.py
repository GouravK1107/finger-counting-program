import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load MediaPipe Hand Landmarker model
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.7,
    min_hand_presence_confidence=0.7,
    min_tracking_confidence=0.7
)


landmarker = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

print("Finger Counter Started")
print("Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip camera horizontally for natural view
    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_frame
    )

    result = landmarker.detect(mp_image)

    if result.hand_landmarks:
        hand_landmarks = result.hand_landmarks[0]
        lm_list = []

        h, w, _ = frame.shape

        for id, lm in enumerate(hand_landmarks):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((id, cx, cy))
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        fingers = []

        # Thumb (horizontal check)
        handedness = result.handedness[0][0].category_name

        # Thumb logic based on hand type
        if handedness == "Right":
            if lm_list[4][1] > lm_list[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        else:  # Left hand
            if lm_list[4][1] < lm_list[3][1]:
                fingers.append(1)
            else:
                fingers.append(0)


        # Other four fingers (vertical check)
        for i in range(1, 5):
            if lm_list[tip_ids[i]][2] < lm_list[tip_ids[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = fingers.count(1)

        cv2.putText(frame, f'Fingers: {total_fingers}',
                    (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2,
                    (255, 0, 0),
                    3)

    cv2.imshow("Finger Counter", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
