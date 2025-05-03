# app.py
import streamlit as st
import pandas as pd

# --- Company Info ---
st.title('Happy Rides - Inventory Management Dashboard')
st.subheader('Authorized Dealer: Bounce 1 Electric Pvt Ltd')

company_info = {
    'Company Name': 'Happy Rides',
    'Address': 'MIG 793, Double Road, Mother Dairy Rd, B Sector, Yelahanka New Town, Bengaluru, Karnataka - 560064',
    'GST Number': '29AAQFH2709F1Z7',
    'Phone Number': '8088615473',
    'PAN Number': 'AAQFH2709F'
}

for key, value in company_info.items():
    st.write(f"**{key}:** {value}")

st.markdown("---")

# --- Locations & Agents ---
st.header('Locations & Agents')

locations = {
    'Yelahanka': [('Mahanthesh', '9108736692')],
    'JP Nagara': [('Sreeranga R', '8088615473'), ('Ravichandra', '9573588514')],
    'Nelamanagala': [('Ajith', '6364452411')],
    'Rajajinagara': [('Charan', '8548043036')]
}

for location, agents in locations.items():
    st.subheader(f"📍 {location}")
    for agent in agents:
        st.write(f"- {agent[0]} (📞 {agent[1]})")

st.markdown("---")

# --- Admin Contact ---
st.header('Admin Contact')
st.write("**Sreeranga** (📞 8088615473)")

st.markdown("---")

# --- Sample Inventory Data ---
st.header('Sample Inventory Summary')

data = {
    'Vehicle Model': ['Bounce Infinity E1', 'Bounce Infinity E1+'],
    'Available Units': [25, 15],
    'Booked Units': [10, 5]
}

df = pd.DataFrame(data)
st.table(df)

st.success('Dashboard ready! You can update inventory data as needed.')
