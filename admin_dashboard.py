import streamlit as st
import mysql.connector
import pandas as pd
import os
from db import get_connection   # ✅ koneksi DB


# --- BERANDA ---
def show_dashboard():
    st.subheader("Selamat Datang di Dashboard Admin")
    st.info("Anda login sebagai Admin. Anda memiliki akses penuh ke sistem.")


    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Puskesmas", "-")
    col2.metric("Total Data Input", "-")
    col3.metric("User Aktif", "-")


# --- MANAJEMEN USER ---
def kelola_user():
    st.subheader("👤 Manajemen User")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, username, role FROM users")
    users = cursor.fetchall()

    if users:
        df_users = pd.DataFrame(users)
        st.dataframe(df_users, height=300)

        st.markdown("### ❌ Hapus User")
        user_ids = [str(u["id"]) + " - " + u["username"] for u in users]
        user_to_delete = st.selectbox("Pilih user untuk dihapus", user_ids)

        if st.button("Hapus User"):
            user_id = user_to_delete.split(" - ")[0]
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            conn.commit()
            st.success("✅ User berhasil dihapus")
            st.rerun()
    else:
        st.info("Belum ada user.")

    st.markdown("### ➕ Tambah User Baru")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")
    new_role = st.selectbox("Role", ["user", "admin"])

    if st.button("Tambah User"):
        if new_username and new_password:
            cursor.execute(
                "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)",
                (new_username, new_password, new_role)
            )
            conn.commit()
            st.success(f"✅ User {new_username} berhasil ditambahkan")
            st.rerun()
        else:
            st.error("Username & Password wajib diisi!")

    conn.close()


# --- MANAJEMEN FILE ---
def manajemen_file():
    st.subheader("📂 Daftar File yang Diupload")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM uploads ORDER BY uploaded_at DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        st.info("Belum ada file yang diupload.")
        return

    df = pd.DataFrame(rows)
    df["uploaded_at"] = pd.to_datetime(df["uploaded_at"]).dt.strftime("%d-%m-%Y %H:%M:%S")

    if "id" in df.columns:
        df = df.drop(columns=["id"])

    st.dataframe(df, use_container_width=True, hide_index=True)

    for row in rows:
        with st.expander(f"📌 {row['filename']} ({row['jenis']})"):
            st.write(f"👤 User: **{row['username']}**")
            st.write(f"🕒 Uploaded: {row['uploaded_at']}")
            st.write(f"📂 Path: `{row['filepath']}`")

            file_path = row['filepath']

            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download File",
                        data=f,
                        file_name=row["filename"],
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            else:
                st.error("❌ File tidak ditemukan di server.")

            if st.button(f"🗑 Hapus {row['filename']}", key=f"del_{row['id']}"):
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)

                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM uploads WHERE id = %s", (row['id'],))
                    conn.commit()
                    conn.close()

                    st.success(f"✅ File {row['filename']} berhasil dihapus.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Gagal hapus file: {e}")


# --- LOGOUT ---
def logout():
    st.session_state.clear()
    st.success("Anda berhasil logout.")
    st.rerun()


# --- DASHBOARD UTAMA ---
def admin_dashboard():
    st.title("🏥 Dashboard Admin SiSehat")

    # 👉 Hilangkan Navigasi umum (Home & Logout), langsung ke Menu Admin
    st.sidebar.markdown("🛠️ **Menu Admin**")
    menu = st.sidebar.radio(
        "Menu Admin",
        ["🏠 Survei Sistem", "👤 Manajemen User", "📂 Manajemen File", "📊 Hasil SPM"],
        label_visibility="collapsed"
    )

    if menu == "🏠 Survei Sistem":
        show_dashboard()
    elif menu == "👤 Manajemen User":
        kelola_user()
    elif menu == "📂 Manajemen File":
        manajemen_file()
    elif menu == "📊 Hasil SPM":
        st.write("📊 Halaman hasil SPM (coming soon)")

    # 👉 Tombol logout dipindah ke bawah sidebar (lebih rapi)
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Logout"):
        logout()

