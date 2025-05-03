# app.py
import streamlit as st

# --- Page Config ---
st.set_page_config(
    page_title="Happy Rides - Inventory Dashboard",
    page_icon="🚗",
    layout="wide",
)

# --- Title & Dealer Info ---
st.title("🚗 Happy Rides - Inventory Management Dashboard")
st.subheader("Authorized Dealer: Bounce 1 Electric Pvt Ltd")

st.markdown("""
**Company Name:** Happy Rides  
**Address:** MIG 793, Double Road, Mother Dairy Rd, B Sector, Yelahanka New Town, Bengaluru, Karnataka - 560064  

**GST Number:** 29AAQFH2709F1Z7  
**Phone Number:** 8088615473  
**PAN Number:** AAQFH2709F  
""")

st.divider()

# --- Locations & Agents ---
st.subheader("📍 Locations & Agents")

st.markdown("### 📍 **Yelahanka**")
st.markdown("- Mahantesh 📞 **9108736692**")

st.markdown("### 📍 **JP Nagara**")
st.markdown("- Sreeranga R 📞 **8088615473**")
st.markdown("- Ravichandra 📞 **9573588514**")

st.markdown("### 📍 **Nelamangala**")
st.markdown("- Ajith 📞 **6364452411**")
