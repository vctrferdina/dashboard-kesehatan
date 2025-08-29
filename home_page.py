import streamlit as st

def home_page():
    # CSS Styling
    st.markdown("""
        <style>
        /* Background utama */
        .main {
            background: linear-gradient(135deg, #f0f7ff, #ffffff);
        }
        /* Title utama */
        .title {
            font-family: 'Segoe UI', sans-serif;
            font-size: 42px;
            font-weight: 800;
            color: #0d47a1;
            text-align: center;
            margin-bottom: 8px;
        }
        .subtitle {
            font-family: 'Segoe UI', sans-serif;
            font-size: 20px;
            font-weight: 400;
            color: #424242;
            text-align: center;
            margin-bottom: 35px;
        }
        /* Card styling */
        .card {
            background-color: #ffffff;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.08);
            text-align: center;
        }
        /* Tombol */
        .stButton>button {
            background: linear-gradient(90deg, #42a5f5, #1e88e5);
            color: white;
            font-size: 17px;
            font-weight: 600;
            padding: 14px 26px;
            border-radius: 10px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #64b5f6, #2196f3);
            transform: translateY(-2px);
            box-shadow: 0 6px 14px rgba(0,0,0,0.15);
        }
        /* Info box */
        .info-box {
            background: #f9fbff;
            padding: 22px;
            border-radius: 14px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 3px 8px rgba(0,0,0,0.05);
        }
        .info-title {
            font-size: 18px;
            font-weight: 600;
            color: #1976d2;
            margin-bottom: 6px;
        }
        .info-desc {
            font-size: 14px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    # Banner
    st.markdown("<div class='title'>🏥 Sistem Informasi Kesehatan</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>SiSehat - Solusi Digital Layanan Kesehatan Puskesmas</div>", unsafe_allow_html=True)

    # Gambar tengah
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.image("foto_dinkes.png", use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Highlight fitur
    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown("<div class='info-box'><div class='info-title'>📊 Rekap Data</div><div class='info-desc'>Pantau data Surveilans, Posbindu, dan SPM secara real-time.</div></div>", unsafe_allow_html=True)
    with colB:
        st.markdown("<div class='info-box'><div class='info-title'>👤 Manajemen User</div><div class='info-desc'>Kelola akun dan peran pengguna dengan mudah dan aman.</div></div>", unsafe_allow_html=True)
    with colC:
        st.markdown("<div class='info-box'><div class='info-title'>📂 Manajemen File</div><div class='info-desc'>Upload, unduh, dan arsipkan data kesehatan secara terintegrasi.</div></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Tombol Login
    colb1, colb2, colb3 = st.columns([2, 2, 2])
    with colb2:
        if st.button("🔑 Login ke Sistem", use_container_width=True):
            st.session_state.show_login = True
            st.rerun()


def home_after_login():
    st.markdown(
        """
        <style>
            .welcome-box {
                background-color: #f4faff;
                padding: 40px;
                border-radius: 14px;
                margin-top: 30px;
                box-shadow: 0 6px 14px rgba(0, 0, 0, 0.08);
                text-align: center;
            }

            .welcome-title {
                font-size: 2.2em;
                font-weight: bold;
                color: #1565c0;
                margin-bottom: 12px;
            }

            .welcome-subtitle {
                font-size: 1.3em;
                color: #333333;
                margin-bottom: 20px;
            }

            .info-alert {
                background-color: #e8f5e9;
                color: #2e7d32;
                padding: 14px;
                border-radius: 10px;
                font-size: 1em;
                margin-top: 25px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    username = st.session_state.get("username", "Pengguna")

    st.markdown(f"""
        <div class="welcome-box">
            <div class="welcome-title">👋 Selamat Datang di <span style="color:#00aaff;">SiSehat</span></div>
            <div class="welcome-subtitle">Halo <b>{username}</b> 🧑‍⚕️👩‍⚕️</div>
            <p>Anda telah berhasil login. Silakan gunakan menu di sebelah kiri untuk melihat <b>Dashboard Hasil SPM</b>, melakukan <b>unggah data</b>, atau <b>mengunduh laporan</b>.</p>
            <div class="info-alert">
                ⚠️ <b>Catatan:</b> Pastikan data yang Anda unggah sesuai format yang telah ditentukan.
            </div>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()
