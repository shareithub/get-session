from telethon import TelegramClient
import os
import asyncio

# Ganti dengan API ID dan API Hash Anda
API_ID = 'CHANGE_YOUR_API_ID'
API_HASH = 'CHANGE_YOUR'
SESSION_DIR = 'sessions'

# Membuat folder sessions jika belum ada
if not os.path.exists(SESSION_DIR):
    os.makedirs(SESSION_DIR)

async def login():
    # MASUKAN NAMA UNTUK FILE SESSION ANDA !
    phone = input("Masukkan Nama untuk file session yang dibuat : ").replace(" ", "")
    
    # Menggunakan nomor telepon sebagai nama session
    session_path = os.path.join(SESSION_DIR, f'{phone}.session')
    
    async with TelegramClient(session_path, API_ID, API_HASH) as client:
        await client.start()

        if await client.is_user_authorized():
            me = await client.get_me()
            print(f"Anda sudah login dengan akun {me.first_name}.")
            return
        
        # Mengirim permintaan kode
        await client.send_code_request(phone)
        code = input("Masukkan kode yang dikirim ke Telegram: ")
        await client.sign_in(phone, code)

        # Ambil nama pengguna
        me = await client.get_me()
        print(f"Login berhasil! File session telah dibuat dengan nama '{phone}.session' di folder 'sessions'.")

async def main():
    await login()

# Menjalankan fungsi utama
if __name__ == "__main__":
    asyncio.run(main())
