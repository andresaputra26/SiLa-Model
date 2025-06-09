# ✋ SiLa Gesture Recognition Model

Notebook ini berisi proses pembuatan dan pelatihan model gesture recognition untuk **Bahasa Isyarat Indonesia (SIBI)** menggunakan MediaPipe dan TensorFlow.

## 📚 Deskripsi Notebook

### Load data dari Google Drive
Dataset berupa file CSV yang berisi koordinat landmark tangan dikumpulkan sebelumnya dan disimpan di Google Drive. Notebook ini menggunakan integrasi `drive.mount()` untuk mengakses folder tersebut dan memuat seluruh file CSV secara otomatis.

### Merge Data
Setiap file CSV merepresentasikan satu gesture tertentu. Semua file digabung menjadi satu DataFrame besar menggunakan `pandas.concat()`. Hasilnya disimpan sebagai `dataset_all.csv` yang menjadi basis data untuk pelatihan model.

## ⚙️ Teknologi yang Digunakan

- TensorFlow / Keras
- MediaPipe
- Pandas, NumPy
- Matplotlib

## 🧪 Langkah-Langkah Utama

1. Load dataset hasil ekstraksi koordinat landmark tangan.
2. Preprocessing data: normalisasi, encoding label.
3. Bangun model: MLP.
4. Training model dan evaluasi.
5. Simpan model ke format `.h5` untuk deployment.

## 📈 Hasil Pelatihan

- **Training Accuracy**: 82.84%
- **Validation Accuracy**: 89.81%

## 📁 Struktur Output

```bash
├── gesture_mlp_model.h5       # Model hasil pelatihan
├── label_encoder.pkl          # Encoder label gesture
├── training_plot.png          # Visualisasi akurasi dan loss
```

## 🚀 Cara Menjalankan

Buka file `.ipynb` ini di Jupyter Notebook atau Google Colab dan jalankan cell secara berurutan.

## 📝 Catatan

- Dataset harus sudah tersedia dalam format CSV dengan kolom koordinat landmark dan label gesture.
- Gunakan MediaPipe Hands untuk membuat dataset gesture jika belum tersedia.
