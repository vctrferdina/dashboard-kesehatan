import streamlit as st
from sidebar_page import sidebar_menu
from user_dashboard import user_dashboard
from admin_dashboard import admin_dashboard

# Simulasi role login
role = st.sidebar.selectbox("Pilih role login", ["user", "admin"])

menu = sidebar_menu(role)

# Routing sesuai role
if role == "user":
    user_dashboard(menu)
elif role == "admin":
    admin_dashboard(menu)