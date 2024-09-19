import os
from pyrogram import Client
import asyncio

# Ganti dengan API ID dan API Hash kamu
api_id = 'CHANGE YOUR API ID'  # API ID
api_hash = 'CHANGE YOUR HASH ID'  # API Hash

async def main():
    print("Login menggunakan nomor telepon")
    
    # Meminta input nomor telepon
    phone_number = input("Masukkan nomor telepon: ")
    
    # Menghapus spasi dari nomor telepon
    phone_number = phone_number.replace(" ", "")
    
    # Membuat folder sessions jika belum ada
    session_dir = "sessions"
    os.makedirs(session_dir, exist_ok=True)

    # Nama file sesi
    session_name = os.path.join(session_dir, phone_number)  # Menyimpan di dalam folder sessions

    # Membuat client
    async with Client(session_name, api_id, api_hash) as app:
        print("Client created. Please log in using your phone number.")
        await app.start()
        await app.send_code_request(phone_number)
        
        # Menerima kode verifikasi dari pengguna
        code = input("Masukkan kode verifikasi yang diterima: ")
        
        # Menyelesaikan proses login
        await app.sign_in(phone_number, code)
        print("Login successful! Session file created:", session_name + '.session')

# Menjalankan fungsi utama
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
