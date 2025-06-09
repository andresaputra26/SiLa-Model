import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
import json

try:
    # Load model
    model = tf.keras.models.load_model("gesture_mlp_model.h5")
    print("[INFO] Model berhasil dimuat.")

    # Load label dari JSON (format dictionary: {label: index})
    with open("label.json", "r") as f:
        label_dict = json.load(f)
    print(f"[INFO] Label list berhasil dimuat: {label_dict}")

    # Fungsi untuk mengembalikan label dari class_id (kebalikan dari dict)
    def inverse_transform(class_id):
        for label, idx in label_dict.items():
            if idx == class_id:
                return label
        return "Unknown"

    # Inisialisasi MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    hands = mp_hands.Hands(static_image_mode=False,
                           max_num_hands=1,
                           min_detection_confidence=0.7,
                           min_tracking_confidence=0.7)

    # Mulai webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Tidak bisa mengakses webcam.")
        exit()

    print("[INFO] Jalankan webcam... tekan 'q' untuk keluar.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Gagal membaca frame dari webcam.")
            break

        # Flip horizontal untuk mirror view
        frame = cv2.flip(frame, 1)

        # Convert ke RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Gambar landmark di frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Ambil (x, y) dari 21 titik (42 fitur)
                landmark_list = []
                for lm in hand_landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y])

                if len(landmark_list) == 42:
                    try:
                        input_data = np.array(landmark_list).reshape(1, -1)
                        prediction = model.predict(input_data)
                        class_id = np.argmax(prediction)
                        label = inverse_transform(class_id)

                        # Tampilkan label di frame
                        cv2.putText(frame, f'Gesture: {label}', (10, 50),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                    except Exception as e:
                        print(f"[ERROR] Gagal prediksi: {e}")

        # Tampilkan frame
        cv2.imshow("Gesture Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Bersihkan
    cap.release()
    cv2.destroyAllWindows()

except Exception as e:
    print(f"[FATAL ERROR] {e}")