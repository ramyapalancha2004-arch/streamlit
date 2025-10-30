import streamlit as st


tab_names = ["Home", "Settings", "About"]
tabs = st.tabs(tab_names)



st.set_page_config(layout="wide")
st.title("🏖️ Travel Gallery")


users = [
    {"name": "Aarav", "age": 12}, {"name": "Priya", "age": 10}, {"name": "Rahul", "age": 14},
    {"name": "Sneha", "age": 19}, {"name": "Kiran", "age": 25}, {"name": "Vikram", "age": 30},
    {"name": "Meera", "age": 35}, {"name": "Raj", "age": 40}, {"name": "Pooja", "age": 45},
    {"name": "Amit", "age": 50}, {"name": "Karthik", "age": 55}, {"name": "Anjali", "age": 60},
    {"name": "Rajesh", "age": 65}, {"name": "Lakshmi", "age": 70}, {"name": "Sundar", "age": 75},
    {"name": "Suresh", "age": 80}, {"name": "Kamala", "age": 85}, {"name": "Mohan", "age": 90},
    {"name": "Leela", "age": 95}, {"name": "Raman", "age": 100},
]


with st.sidebar:
    st.header("Select Age Range")
    age_ranges = ["0-15", "16-25", "26-50", "51-75", "76-100", "All"]
    selected_range = st.selectbox("Age Range:", age_ranges)


if "open_section" not in st.session_state:
    st.session_state.open_section = None

def toggle_section(name):
    """Only one info section open at a time."""
    if st.session_state.open_section == name:
        st.session_state.open_section = None
    else:
        st.session_state.open_section = name


col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Info1"):
        toggle_section("Info1")
with col2:
    if st.button("Info2"):
        toggle_section("Info2")
with col3:
    if st.button("Info3"):
        toggle_section("Info3")

st.markdown("---")  

if st.session_state.open_section == "Info1":
    col1_1, col1_2 = st.columns(2)
    with col1_1:
        st.image("https://images.unsplash.com/photo-1582719478250-c89cae4dc85b", use_container_width=True)
        st.caption("Goa")
    with col1_2:
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_container_width=True)
        st.caption("Bali")

elif st.session_state.open_section == "Info2":
    col2_1, col2_2 = st.columns(2)
    with col2_1:
        st.image("https://discoverkullumanali.in/wp-content/uploads/2015/07/Hidimba-Devi-Temple-Manali-800x530.jpg", use_container_width=True)
        st.caption("Manali")
    with col2_2:
        st.image("https://images.unsplash.com/photo-1502602898657-3e91760cbb34", use_container_width=True)
        st.caption("Paris")

elif st.session_state.open_section == "Info3":
    col3_1, col3_2 = st.columns(2)
    with col3_1:
        st.image("https://www.vacationstravel.com/wp-content/uploads/2021/10/shutterstock_1281956065.jpg", use_container_width=True)
        st.caption("Tokyo")
    with col3_2:
        st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", use_container_width=True)
        st.caption("Bali")

if selected_range != "All":
    start, end = map(int, selected_range.split("-"))
    filtered_users = [u for u in users if start <= u["age"] <= end]
else:
    filtered_users = users

st.divider()
st.subheader(f"Users in Age Range: {selected_range} yrs ({len(filtered_users)} found)")
if filtered_users:
    st.markdown(", ".join([u['name'] for u in filtered_users]))
else:
    st.write("No users in this age range.")
