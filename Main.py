import streamlit as st
from streamlit_modal import Modal

# Title and divider underneath it
st.title(":green[SHAREON]")
st.divider()

# To allow user to enter location and change listings based on that
st.text_input('Your Location:', placeholder="Postal Code")

# Available listings and the number is supposed to be changing based on the number of available listings
col1, col2 = st.columns(2)

with col1:
    st.text("Available Listings:")

with col2:
    st.text("1")

st.divider()

itemCard = st.container()

with itemCard:
    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        st.image("https://www.thespruce.com/thmb/AmoHdun9LM_HiRPRSEuKHByN6s8=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/spr-primary-drills-dburreson-001-02d983fd8e5f42ae8d8b5d799baca68a.jpg")
    with col2:
        more_info = Modal("More info", key="more_info")
        contactInfo = Modal("Contact", key="contactInfo")
        st.text("Drill")
        st.text("Status: Available")
        st.text("Loaner: Ryan Tan")
        openInfo = st.button("More info")
        openContact = st.button("Contact")
        if openInfo:
            with more_info.container():
                st.text("This is a drill tf more u want cb, suck my dick. brokie mofo - xoxo Ryan Tan")

        if openContact:
            with contactInfo.container():
                st.text("+65 999")
                st.text("mindyourownbusiness@suckacock.com")

st.divider()
