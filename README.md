## CAPAPP MEGAETH TESNET

## Fitur

- **Auto Mint Token cUSD**
- **Integrasi Telegram**: Mengirim notifikasi langsung ke pengguna melalui bot Telegram.
- **Konfigurasi Mudah**: Menggunakan file `.env` untuk menyimpan konfigurasi sensitif seperti token dan API key.

## Struktur Proyek

```
capappSHM/
├── .env               
├── .gitignore         
├── bot.py             
├── requirements.txt   
└── wallets.json       
```

## Instalasi

1. **Klon repositori ini**:

   ```bash
   git clone https://github.com/rexi-ctrl/capappSHM.git
   cd capappSHM
   ```

2. **Instal dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Konfigurasi file **``:

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
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" },
  { "address": "", "private_key": "" }
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

## X ACCOUNT

https://x.com/belchman_

## Lisensi

Proyek ini dilisensikan di bawah MIT License.

