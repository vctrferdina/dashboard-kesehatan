import streamlit as st
from db import get_connection  

def login_page():
    # Styling CSS
    st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 40px auto;
            padding: 35px 30px;
            background: #ffffff;
            border-radius: 16px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        }
        .login-title {
            text-align: center;
            font-size: 28px;
            font-weight: 700;
            color: #1565c0;
            margin-bottom: 8px;
        }
        .login-subtitle {
            text-align: center;
            font-size: 15px;
            color: #666;
            margin-bottom: 25px;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stButton>button {
            width: 100%;
            border-radius: 10px;
            background: linear-gradient(90deg, #42a5f5, #1e88e5);
            color: white;
            font-weight: 600;
            font-size: 16px;
            padding: 12px 0;
            transition: 0.3s;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #64b5f6, #2196f3);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # Card Login
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='login-title'>🔐 Login</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-subtitle'>Masukkan kredensial untuk mengakses sistem</div>", unsafe_allow_html=True)

    # Input username & password
    username = st.text_input("👤 Username", key="username_input")
    password = st.text_input("🔑 Password", type="password", key="password_input")

    # Tombol Login
    if st.button("Login", key="login_btn"):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            st.session_state.logged_in = True
            st.session_state.username = user["username"]
            st.session_state.role = user["role"]
            st.session_state.show_login = False  # langsung hilangkan form login
            st.success(f"✅ Login berhasil! Selamat datang, {user['username']}")
            st.rerun()
        else:
            st.error("❌ Username atau password salah.")

    # Tombol kembali ke home
    if st.button("⬅️ Kembali ke Beranda", key="back_btn"):
        st.session_state.show_login = False   # balik ke home_page()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
