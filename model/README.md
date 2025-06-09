# Backend FastAPI SiLa

API Backend untuk **SiLa – Sign Language Application**, aplikasi pengenalan Bahasa Isyarat Indonesia secara real-time menggunakan klasifikasi landmark tangan berbasis MLP.

## Teknologi yang Digunakan

- **Backend**: FastAPI (Python)
- **Model ML**: TensorFlow (`.h5` format)
- **Deployment**: Railway / Uvicorn
- **Gaya API**: RESTful
- **Middleware**: CORS (FastAPI)
- **Input Model**: Vektor landmark (42 nilai float)

## Langkah Instalasi

1. Clone repositori ini
2. Buat dan aktifkan environment virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # di Windows: venv\Scripts\activate
   ```
3. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
4. Buat folder `model/` dan tambahkan:
   - `gesture_mlp_model.h5` — file model terlatih
   - `label.json` — file mapping label ke karakter

5. Jalankan server lokal:
   ```bash
   uvicorn main:app --reload
   ```

## Variabel Lingkungan (Opsional)

Jika menggunakan layanan seperti Railway, tambahkan variabel berikut:

```
PORT=8000
```

## Endpoint API

### `POST /predict`

**Deskripsi**: Memprediksi karakter bahasa isyarat dari 42 nilai landmark tangan.

#### Contoh Request Body

```json
{
  "landmarks": [0.123, 0.456, ..., 0.789]  // tepat 42 nilai float
}
```

#### Contoh Response

```json
{
  "label": "A",
  "confidence": 0.9876
}
```

#### Kemungkinan Error

- **Jumlah input tidak sesuai**:
```json
{
  "detail": "Expected 42 values for landmarks"
}
```

- **Error internal server**:
```json
{
  "detail": "Internal Server Error: <pesan error>"
}
```

## Catatan Deployment

- Backend ini dapat dideploy ke Railway, Render, Fly.io, atau server lain.
- Pastikan folder `model/` dan file model tersedia di server.
- Uvicorn akan menggunakan `PORT` dari variabel lingkungan.

## Rencana Pengembangan

- Menambahkan endpoint `/health` untuk monitoring
- Implementasi autentikasi (contoh: JWT)
- Dukungan input sekuensial (untuk model CNN 1D / LSTM)
- Logging prediksi dan versi model

## Struktur Proyek

```
.
├── main.py
├── requirements.txt
├── model/
│   ├── gesture_mlp_model.h5
│   └── label.json
```

---

> Dibuat untuk **SiLa – Sign Language Application** 💡 Menghubungkan komunikasi melalui teknologi.