import streamlit as st
import os

# --- Folder penyimpanan file ---
FOLDER_SURVEILANS = "uploads/surveilans"
FOLDER_POSBINDU = "uploads/posbindu"
os.makedirs(FOLDER_SURVEILANS, exist_ok=True)
os.makedirs(FOLDER_POSBINDU, exist_ok=True)


# --- HOME ---
def show_home():
    st.subheader("Selamat Datang di Dashboard User")
    st.info("Silakan unggah data Surveilans atau Posbindu dalam format Excel (.xls / .xlsx)")


# --- UPLOAD SURVEILANS ---
def upload_surveilans():
    st.subheader("📊 Unggah Data Surveilans")
    uploaded_file = st.file_uploader("Pilih file Excel (.xls / .xlsx)", type=["xls", "xlsx"])

    if uploaded_file is not None:
        save_path = os.path.join(FOLDER_SURVEILANS, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File {uploaded_file.name} berhasil diunggah ke folder Surveilans!")


# --- UPLOAD POSBINDU ---
def upload_posbindu():
    st.subheader("🩺 Unggah Data Posbindu")
    uploaded_file = st.file_uploader("Pilih file Excel (.xls / .xlsx)", type=["xls", "xlsx"])

    if uploaded_file is not None:
        save_path = os.path.join(FOLDER_POSBINDU, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ File {uploaded_file.name} berhasil diunggah ke folder Posbindu!")


# --- HASIL SPM ---
def hasil_spm():
    st.subheader("📈 Hasil SPM")
    st.info("Fitur ini untuk menampilkan hasil SPM (akan dihubungkan ke database).")


# --- LOGOUT ---
def logout():
    st.session_state.clear()
    st.success("Anda berhasil logout.")
    st.rerun()


# --- DASHBOARD USER ---
def user_dashboard():
    st.title("🏥 Dashboard User SiSehat")

    menu = st.sidebar.radio(
        "📌 Navigasi",
        ["Home", "Unggah Surveilans", "Unggah Posbindu", "Hasil SPM", "Logout"]
    )

    if menu == "Home":
        show_home()
    elif menu == "Unggah Surveilans":
        upload_surveilans()
    elif menu == "Unggah Posbindu":
        upload_posbindu()
    elif menu == "Hasil SPM":
        hasil_spm()
    elif menu == "Logout":
        logout()


if __name__ == "__main__":
    user_dashboard()