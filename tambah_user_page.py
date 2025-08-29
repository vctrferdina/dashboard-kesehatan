import streamlit as st
from db import get_connection

def add_user(username, role):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, role) VALUES (%s, %s)", (username, role))
    conn.commit()
    conn.close()

def run():
    st.subheader("➕ Tambah Pengguna Baru")

    username = st.text_input("Username")
    role = st.selectbox("Role", ["admin", "user"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Kembali"):
            st.session_state.tambah_user_mode = False
            st.rerun()

    with col2:
        if st.button("💾 Simpan"):
            if not username.strip():
                st.warning("⚠️ Username tidak boleh kosong.")
            else:
                try:
                    add_user(username.strip(), role)
                    st.success(f"✅ User '{username}' berhasil ditambahkan.")
                    st.session_state.tambah_user_mode = False
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Gagal menambahkan user: {e}")