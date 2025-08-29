import streamlit as st
import os
import datetime
from db import get_connection   # ✅ Koneksi DB

# === Folder utama upload ===
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# --- Fungsi simpan file ke folder ---
def save_uploaded_file(file, folder, username):
    user_folder = os.path.join(UPLOAD_FOLDER, username, folder)
    os.makedirs(user_folder, exist_ok=True)

    filename = f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}_{file.name}"
    file_path = os.path.join(user_folder, filename)

    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    return filename, file_path


# --- Fungsi simpan metadata ke DB ---
def save_to_db(username, jenis, filename, filepath):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO uploads (username, jenis, filename, filepath, uploaded_at) 
        VALUES (%s, %s, %s, %s, NOW())
        """,
        (username, jenis, filename, filepath)
    )
    conn.commit()
    conn.close()


# --- Halaman Upload Surveilans ---
def upload_surveilans_page(username):
    st.title("📤 Upload Data Surveilans")
    st.markdown(f"Unggah file Excel untuk Surveilans - **{username}**")

    file = st.file_uploader("Upload File Surveilans", type=["xlsx"], key="surveilans")

    if file is not None:
        if st.button("✅ Simpan / Upload Data Surveilans"):
            filename, path = save_uploaded_file(file, "surveilans", username)
            save_to_db(username, "surveilans", filename, path)
            st.success(f"✅ Data berhasil diupload ke: `{path}`")

    if st.button("🔙 Kembali ke Dashboard", key="back_surveilans"):
        st.session_state.page = "dashboard"
        st.rerun()


# --- Halaman Upload Posbindu ---
def upload_posbindu_page(username):
    st.title("📤 Upload Data Posbindu")
    st.markdown(f"Unggah file Excel untuk Posbindu - **{username}**")

    file = st.file_uploader("Upload File Posbindu", type=["xlsx"], key="posbindu")

    if file is not None:
        if st.button("✅ Simpan / Upload Data Posbindu"):
            filename, path = save_uploaded_file(file, "posbindu", username)
            save_to_db(username, "posbindu", filename, path)
            st.success(f"✅ Data berhasil diupload ke: `{path}`")

    if st.button("🔙 Kembali ke Dashboard", key="back_posbindu"):
        st.session_state.page = "dashboard"
        st.rerun()


# --- Halaman Upload SPM ---
def hasil_spm_page(username):
    st.title("📤 Upload Data Standar Pelayanan Minimal (SPM)")
    st.markdown(f"Unggah file Excel untuk SPM - **{username}**")

    file = st.file_uploader("Upload File SPM", type=["xlsx"], key="spm")

    if file is not None:
        if st.button("✅ Simpan / Upload Data SPM"):
            filename, path = save_uploaded_file(file, "spm", username)
            save_to_db(username, "spm", filename, path)
            st.success(f"✅ Data berhasil diupload ke: `{path}`")

    if st.button("🔙 Kembali ke Dashboard", key="back_spm"):
        st.session_state.page = "dashboard"
        st.rerun()