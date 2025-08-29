from werkzeug.security import generate_password_hash
import mysql.connector

# Koneksi
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sisihat_db"
)
cursor = conn.cursor()

# Username dan password baru (plaintext)
data_users = {
    "admin": "admin123",
    "pkm": "pkm123",
    "puskesmas": "123456",
    "puskesmas kandang": "mantapjiwa",
    "puskesmas muara 2": "puskes123",
    "puskesmas lhokseumawe": "mantapkali123",
    "puskesmas banda sakti": "bairinaja123"
}

# Update hash-nya
for username, plain_password in data_users.items():
    hashed = generate_password_hash(plain_password)
    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (hashed, username))

conn.commit()
cursor.close()
conn.close()

print("✅ Semua password berhasil direset dan di-hash ulang.")
