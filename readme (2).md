# capappSHM

**capappSHM** adalah sebuah aplikasi berbasis Python yang dirancang untuk memantau dan mengelola dompet kripto secara otomatis. Aplikasi ini memungkinkan pengguna untuk mengawasi aktivitas dompet kripto mereka dan memberikan notifikasi melalui bot Telegram.

## Fitur

- **Pemantauan Dompet Kripto**: Mengawasi aktivitas dompet kripto yang ditentukan.
- **Integrasi Telegram**: Mengirim notifikasi langsung ke pengguna melalui bot Telegram.
- **Konfigurasi Mudah**: Menggunakan file `.env` untuk menyimpan konfigurasi sensitif seperti token dan API key.

## Struktur Proyek

```
capappSHM/
├── .env               # File konfigurasi lingkungan
├── .gitignore         # File untuk mengecualikan file dari kontrol versi
├── bot.py             # Skrip utama untuk menjalankan bot Telegram
├── requirements.txt   # Daftar dependensi Python
└── wallets.json       # Daftar dompet kripto yang dipantau
```

## Instalasi

1. **Klon repositori ini**:

   ```bash
   git clone https://github.com/rexi-ctrl/capappSHM.git
   cd capappSHM
   ```

2. **Buat dan aktifkan virtual environment (opsional namun direkomendasikan)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Linux/macOS
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Instal dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi file **``:

   Buat file `.env` di direktori utama dan tambahkan informasi berikut:

   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   API_KEY=your_api_key
   ```

   Gantilah `your_telegram_bot_token` dan `your_api_key` dengan informasi yang sesuai.

5. **Siapkan file **``:

   Buat file `wallets.json` dan tambahkan daftar dompet kripto yang ingin dipantau:

   ```json
   [
     {
       "address": "0xYourWalletAddress1",
       "label": "Dompet Utama"
     },
     {
       "address": "0xYourWalletAddress2",
       "label": "Dompet Cadangan"
     }
   ]
   ```

## Penggunaan

Jalankan bot dengan perintah berikut:

```bash
python bot.py
```

Bot akan mulai memantau dompet yang telah ditentukan dan mengirim notifikasi melalui Telegram jika ada aktivitas yang terdeteksi.

## Kontribusi

Kontribusi sangat diterima! Jika Anda ingin berkontribusi:

1. Fork repositori ini.
2. Buat branch fitur Anda: `git checkout -b fitur-baru`.
3. Commit perubahan Anda: `git commit -m 'Menambahkan fitur baru'`.
4. Push ke branch Anda: `git push origin fitur-baru`.
5. Buat pull request.

## Lisensi

Proyek ini dilisensikan di bawah MIT License.

