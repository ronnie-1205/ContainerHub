import streamlit as st
import json
from pathlib import Path

# Constants
LINKS_FILE = Path("data/links.json")
USERNAME = "admin"
PASSWORD = "password"

# Set wide layout for flexibility
st.set_page_config(page_title="Dashboard", layout="wide")

# Authentication (Simple)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    center_col = st.columns([1, 2, 1])[1]
    with center_col:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
            else:
                st.error("Incorrect username or password.")
    st.stop()

# Load links from JSON
def load_links():
    if LINKS_FILE.exists():
        with open(LINKS_FILE) as f:
            return json.load(f)
    return {}

# Responsive column layout: adjusts based on screen size
def display_links_responsive(links_dict, max_cols=4):
    items = list(links_dict.items())
    n = len(items)
    if n == 0:
        st.info("No links found. Add entries to data/links.json.")
        return

    for i in range(0, n, max_cols):
        cols = st.columns(min(max_cols, n - i))
        for col, (name, url) in zip(cols, items[i:i + max_cols]):
            with col:
                st.link_button(name, url)

# Main centered layout
center_col = st.columns([1, 5, 1])[1]
with center_col:
    st.title("📟 Container Dashboard")
    st.caption("Click a button to open the respective container service.")
    if st.button("🔄 Refresh Links"):
        st.rerun()

    display_links_responsive(load_links(), max_cols=4)
