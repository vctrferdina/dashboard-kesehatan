from werkzeug.security import generate_password_hash
import mysql.connector

# Koneksi ke database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sisihat_db"
)
cursor = conn.cursor()

# Ambil semua user yang password-nya belum di-hash (tidak diawali 'pbkdf2:')
cursor.execute("SELECT id, username, password FROM users WHERE password NOT LIKE 'pbkdf2:%'")
users = cursor.fetchall()

# Proses hashing
for user in users:
    user_id, username, plain_password = user
    hashed_password = generate_password_hash(plain_password)
    cursor.execute("UPDATE users SET password = %s WHERE id = %s", (hashed_password, user_id))
    print(f"🔒 Password untuk user '{username}' berhasil di-hash.")

conn.commit()
cursor.close()
conn.close()
print("✅ Semua password plaintext sudah di-hash.")
