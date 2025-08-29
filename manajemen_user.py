import streamlit as st
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sisihat_db"
    )

def manajemen_user_page():
    st.title("👥 Manajemen User")

    menu = ["Lihat User", "Tambah User"]
    choice = st.radio("Menu", menu)

    conn = get_connection()
    cursor = conn.cursor()

    if choice == "Lihat User":
        cursor.execute("SELECT id, username, role FROM users")
        users = cursor.fetchall()
        st.table(users)

    elif choice == "Tambah User":
        st.subheader("➕ Tambah Pengguna Baru")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")  # 🔑 tambahin form password
        role = st.selectbox("Role", ["admin", "user"])

        if st.button("Simpan"):
            if username and password:
                cursor.execute(
                    "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                    (username, password, role)
                )
                conn.commit()
                st.success(f"✅ User {username} berhasil ditambahkan!")
            else:
                st.warning("⚠️ Username dan Password wajib diisi!")

    conn.close()