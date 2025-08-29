import streamlit as st

def sidebar_menu(role="user"):
    if role == "admin":
        menu = [
            "Home",
            "Dashboard",
            "Manajemen User",
            "Logout"
        ]
    else:  # role user biasa
        menu = [
            "🏠 Home",
            "📤 Unggah Surveilans",
            "🩺 Unggah Posbindu",
            "📈 Hasil SPM",
            
        ]

    choice = st.sidebar.radio("", menu)
    return choice
