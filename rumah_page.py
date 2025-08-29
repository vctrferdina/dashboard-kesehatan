import streamlit as st

def app(user_info):
    st.title("🏠 Beranda SiSehat")
    
    st.markdown(f"Selamat datang, **{user_info['username']}** 👋")
    st.markdown("Anda login sebagai: `{}`".format(user_info['role']))

    st.markdown("---")
    st.subheader("📊 Ringkasan Data (Dummy)")

    col1, col2, col3 = st.columns(3)
    col1.metric("Jumlah Surveilans", "120")
    col2.metric("Jumlah Posbindu", "85")
    col3.metric("Jumlah SPM", "67")

    st.markdown("---")
    st.subheader("📌 Petunjuk Penggunaan")
    st.markdown("""
    - Gunakan menu di kiri untuk mengunggah data Surveilans, Posbindu, dan SPM.
    - Pastikan file dalam format `.xlsx` atau `.csv` sesuai template.
    - Data akan divalidasi secara otomatis setelah diunggah.
    """)

    st.markdown("---")
    st.info("⚠️ Batas waktu unggah data bulanan: Tanggal 15 setiap bulan.")
    
if __name__ == "__main__":
    home_page()
