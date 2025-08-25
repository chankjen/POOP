import streamlit as st
import pandas as pd

# 1. Page config
st.set_page_config(
    page_title="Ubuntu Hospital Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar filters
st.sidebar.header("Controls")
dept = st.sidebar.selectbox(
    "Select Department",
    ["Emergency", "Cardiology", "Radiology", "Pharmacy"]
)
severity = st.sidebar.slider(
    "Filter by Triage Severity",
    min_value=1,
    max_value=5,
    value=(1, 5)
)

# 3. Fake data for demo
rooms_data = [
    {"room": "ER-101", "type": "Trauma", "occupied": False},
    {"room": "ER-102", "type": "Exam",   "occupied": True},
    {"room": "ER-103", "type": "Proc",   "occupied": False},
]
eq_data = [
    {"name": "X-Ray", "status": "Ready"},
    {"name": "Ultrasound", "status": "Due for Maint."},
    {"name": "EKG", "status": "Ready"},
]
rooms_df = pd.DataFrame(rooms_data)
eq_df    = pd.DataFrame(eq_data)

# 4. Main dashboard
st.title(f"🏥 Ubuntu Hospital — {dept} Department")
st.markdown("### Room Availability")
available = rooms_df[~rooms_df["occupied"]]
occupied  = rooms_df[rooms_df["occupied"]]

col1, col2 = st.columns(2)
with col1:
    st.metric("Available Rooms", len(available), delta=None)
    st.dataframe(available.set_index("room"))
with col2:
    st.metric("Occupied Rooms", len(occupied), delta=None)
    st.dataframe(occupied.set_index("room"))

st.markdown("---")
st.markdown("### Equipment Status")
st.table(eq_df.set_index("name"))

# 5. Footer / Notes
st.markdown(
    """
    **Notes:**  
    - Use the sidebar to switch departments.  
    - Triage slider (1=Immediate, 5=Non-Urgent) will filter live admissions.  
    - Click on any room or equipment row to see detailed history (coming soon!).
    """
)
