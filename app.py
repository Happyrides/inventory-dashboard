# app.py
import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(
    page_title="Happy Rides - Inventory Dashboard",
    page_icon="🚗",
    layout="wide",
)

# --- Title & Dealer Info ---
st.title("🚗 Happy Rides - Inventory Management Dashboard")
st.subheader("Authorized Dealer: Bounce 1 Electric Pvt Ltd")

# --- Company Info Table ---
company_info = {
    'Field': ['Company Name', 'Address', 'GST Number', 'Phone Number', 'PAN Number'],
    'Details': [
        'Happy Rides',
        'MIG 793, Double Road, Mother Dairy Rd, B Sector, Yelahanka New Town, Bengaluru, Karnataka - 560064',
        '29AAQFH2709F1Z7',
        '8088615473',
        'AAQFH2709F'
    ]
}
company_df = pd.DataFrame(company_info)
st.table(company_df)

st.divider()

# --- Locations & Agents ---
st.subheader("📍 Locations & Agents")

# Yelahanka
st.markdown("### 📍 **Yelahanka**")
yelahanka_agents = {
    'Agent Name': ['Mahantesh'],
    'Phone Number': ['9108736692']
}
st.table(pd.DataFrame(yelahanka_agents))

# JP Nagara
st.markdown("### 📍 **JP Nagara**")
jp_nagara_agents = {
    'Agent Name': ['Sreeranga R', 'Ravichandra'],
    'Phone Number': ['8088615473', '9573588514']
}
st.table(pd.DataFrame(jp_nagara_agents))

# Nelamangala
st.markdown("### 📍 **Nelamangala**")
nelamangala_agents = {
    'Agent Name': ['Ajith'],
    'Phone Number': ['6364452411']
}
st.table(pd.DataFrame(nelamangala_agents))
