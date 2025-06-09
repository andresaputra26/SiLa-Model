# 🖐️ Landmark Data Collection with MediaPipe

Script ini digunakan untuk merekam data koordinat landmark tangan menggunakan webcam dan MediaPipe Hands, kemudian menyimpannya sebagai file CSV untuk keperluan pelatihan model machine learning seperti gesture recognition.

## 📁 Struktur File

```bash
.
├── collect_landmark_data.py
├── dataset/
│   └── [gesture_label].csv
```

## 📦 Dependencies

Pastikan Python sudah terinstal, lalu install dependencies berikut:

```bash
pip install opencv-python mediapipe pandas
```

## 🚀 Cara Menjalankan

Untuk merekam gesture tertentu (contoh: "space"):

```bash
python collect_landmark_data.py
```

Atau modifikasi baris terakhir file:

```python
if __name__ == "__main__":
    collect_landmark_data("space", samples=200)
```

Gantilah "space" dengan label lain seperti "A", "B", dll sesuai gesture yang ingin kamu kumpulkan.

## 🎯 Fitur Utama

- Menggunakan **MediaPipe Hands** untuk mendeteksi 21 titik landmark tangan.
- Setiap data yang dikumpulkan terdiri dari 42 fitur (x dan y dari 21 titik) + label gesture.
- Real-time visual feedback dengan OpenCV.
- Tekan `q` untuk menghentikan proses lebih awal.

## 📊 Format Output

CSV akan tersimpan dalam folder `dataset/` dengan format:

| x0  | y0  | x1  | y1  | ... | x20 | y20 | label |
|-----|-----|-----|-----|-----|-----|-----|-------|
| 0.1 | 0.2 | 0.3 | 0.4 | ... | ... | ... |  A    |

## 📝 Catatan

- `samples` menentukan jumlah data yang dikumpulkan per label.
- Pastikan pencahayaan cukup agar deteksi tangan optimal.
- Hanya satu tangan yang dideteksi (`max_num_hands=1`).

## 📷 Tampilan

Saat dijalankan, webcam akan aktif dan jendela akan menampilkan:

- Kerangka tangan (hand skeleton).
- Jumlah data yang sudah direkam.
- Tekan `q` untuk keluar lebih awal.
