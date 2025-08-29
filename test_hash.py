from werkzeug.security import check_password_hash

# Isi dengan password hash dari database (copas salah satu hash yang ada di phpMyAdmin)
hashed_pw = "scrypt:32768:8:1$3FMyGLIJ7y1cd1Dr$f5b7c5edf48db55ea27b2c08845f457d29830ca9653e7f0c5d3bcde53fba97597c5735161a79696616e63803e2b3b2a0708bd7f720b22702cf4c8f79e39b164d"

# Password asli yang ingin dicek
password_input = "admin123"

# Cek apakah password cocok
if check_password_hash(hashed_pw, password_input):
    print("Password cocok!")
else:
    print("Password salah!")
