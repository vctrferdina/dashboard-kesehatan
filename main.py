import streamlit as st

# Import halaman dan modul
from sidebar_page import sidebar_menu
from home_page import home_page, home_after_login  
from login_page import login_page
from admin_dashboard import admin_dashboard
from manajemen_user import manajemen_user_page
from upload_page import upload_surveilans_page, upload_posbindu_page, hasil_spm_page
from user_dashboard import user_dashboard   # << tambahan import ini

def main():
    # --- Inisialisasi session state ---
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "show_login" not in st.session_state:
        st.session_state.show_login = False
    if "username" not in st.session_state:
        st.session_state.username = "Guest"
    if "role" not in st.session_state:
        st.session_state.role = "user"
    if "tambah_user_mode" not in st.session_state:
        st.session_state.tambah_user_mode = False

    # --- Styling sidebar ---
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            background-color: #E3F2FD;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Kalau belum login ---
    if not st.session_state.logged_in:
        if st.session_state.show_login:
            login_page()
        else:
            home_page()

    # --- Kalau sudah login ---
    else:
        with st.sidebar:
            st.markdown(
                f"👤 Login sebagai: `{st.session_state.username}` ({st.session_state.role})"
            )

            # Ambil menu, tapi exclude Logout dari radio button
            menu = sidebar_menu(role=st.session_state.role)

            st.markdown("---")

            # Tombol logout terpisah di bawah sidebar
            if st.button("Logout"):
                st.session_state.clear()
                st.rerun()

        # Render konten sesuai menu yang dipilih
        if menu == "Home" or menu == "🏠 Home":
            home_after_login()

        elif menu == "Dashboard":
            admin_dashboard()

        elif menu == "Unggah Surveilans" or menu == "📤 Unggah Surveilans":
            if st.session_state.role == "user":
                user_dashboard(menu)
            else:
                upload_surveilans_page(st.session_state.username)

        elif menu == "Unggah Posbindu" or menu == "🩺 Unggah Posbindu":
            if st.session_state.role == "user":
                user_dashboard(menu)
            else:
                upload_posbindu_page(st.session_state.username)

        elif menu == "Hasil SPM" or menu == "📈 Hasil SPM":
            if st.session_state.role == "user":
                user_dashboard(menu)
            else:
                hasil_spm_page()

        elif menu == "Manajemen User":
            if st.session_state.role == "admin":
                manajemen_user_page()
            else:
                st.warning("⚠️ Anda tidak memiliki akses ke Manajemen User.")

        # Jangan lagi cek menu == Logout karena sudah terpisah tombol logout


if __name__ == "__main__":
    main()
