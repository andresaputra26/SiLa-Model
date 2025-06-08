import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
import json

def train_mlp_model(dataset_path="dataset_all.csv"):
    # Load dataset
    data = pd.read_csv(dataset_path)
    X = data.drop("label", axis=1).values
    y = data["label"].values

    # Label Encoding
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Simpan label ke JSON
    label_mapping = {label: int(idx) for idx, label in enumerate(le.classes_)}
    with open("label.json", "w") as f:
        json.dump(label_mapping, f)
    print("[INFO] label.json disimpan.")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

    # Definisikan model MLP
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(len(le.classes_), activation='softmax')  # Kelas dinamis
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Training
    model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)

    # Evaluasi
    loss, acc = model.evaluate(X_test, y_test)
    print(f"[RESULT] Akurasi pada data uji: {acc*100:.2f}%")

    # Simpan model
    model.save("gesture_mlp_model.h5")
    print("[INFO] Model disimpan sebagai gesture_mlp_model.h5")

if __name__ == "__main__":
    train_mlp_model()
