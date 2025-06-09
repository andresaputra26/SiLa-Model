# ✋ Real-time Gesture Detection with MLP & MediaPipe

`test.py` digunakan untuk mendeteksi gesture tangan secara real-time melalui webcam menggunakan model Machine Learning yang telah dilatih sebelumnya (`gesture_mlp_model.h5`). Proses deteksi dilakukan berdasarkan 21 titik landmark dari tangan yang diperoleh melalui MediaPipe Hands.

## 📁 Struktur File

```bash
.
├── test.py                     # Script deteksi gesture
├── gesture_mlp_model.h5       # Model hasil pelatihan
├── label.json                 # File JSON berisi label -> index
```

## 📦 Dependencies

Pastikan kamu sudah menginstall:

```bash
pip install opencv-python mediapipe tensorflow numpy
```

## 🚀 Cara Menjalankan

```bash
python test.py
```

## 📥 Input

- Webcam aktif.
- Deteksi landmark tangan secara real-time (hanya satu tangan).
- Model menerima 42 fitur input: `(x0, y0, x1, y1, ..., x20, y20)`.

## 📤 Output

- Label gesture ditampilkan di layar.
- Tekan `q` untuk keluar.

## 🧠 Fungsi Utama

- `model.predict()` digunakan untuk memprediksi gesture berdasarkan input landmark.
- Label dikembalikan ke bentuk string menggunakan file `label.json` (dalam bentuk dictionary `{label: index}`).
- Menggunakan OpenCV untuk menampilkan visual frame dengan overlay hasil prediksi dan skeleton tangan.

## 📝 Catatan Tambahan

- Jika webcam gagal diakses, akan ditampilkan error `[ERROR] Tidak bisa mengakses webcam.`
- Jika prediksi gagal, akan tetap dijalankan tanpa crash.
- File `label.json` harus sesuai dengan label yang digunakan saat pelatihan model.

## 🧪 Contoh Output

```bash
[INFO] Model berhasil dimuat.
[INFO] Label list berhasil dimuat: {"A": 0, "B": 1, ..., "space": 26}
[INFO] Jalankan webcam... tekan 'q' untuk keluar.
```

Tampilan akan menunjukkan video webcam dengan landmark dan prediksi gesture tangan secara live.
