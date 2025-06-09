import cv2
import mediapipe as mp
import pandas as pd
import os

def collect_landmark_data(gesture_label, samples=200, save_dir="dataset"):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
    mp_draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    data = []
    count = 0

    os.makedirs(save_dir, exist_ok=True)
    print(f"[INFO] Mulai merekam gesture: {gesture_label}")

    while cap.isOpened() and count < samples:
        ret, frame = cap.read()
        if not ret:
            break
        img = cv2.flip(frame, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.extend([lm.x, lm.y])
                data.append(landmarks + [gesture_label])
                count += 1
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv2.putText(img, f"Captured: {count}/{samples}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.imshow("Collecting Landmark Data", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    columns = [f"x{i}" if i % 2 == 0 else f"y{i//2}" for i in range(42)] + ["label"]
    df = pd.DataFrame(data, columns=columns)
    save_path = os.path.join(save_dir, f"{gesture_label}.csv")
    df.to_csv(save_path, index=False)
    print(f"[INFO] Data gesture '{gesture_label}' disimpan di: {save_path}")

if __name__ == "__main__":
    # Contoh: rekam gesture 'A'
    collect_landmark_data("space", samples=200)
