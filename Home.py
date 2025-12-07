import streamlit as st
from PIL import Image

# from auth import authenticator
st.set_page_config(page_title='Urban Fitness Gym',layout='wide')

with st.spinner("Initializing face recognition components"):
    import face_rec

st.header('Attendance System using Face Recognition')

# Welcome admin
st.subheader("Welcome, Admin!")

gym_image = Image.open('gym.jpg')
st.image(gym_image, caption='Urban Fitness Gym', use_column_width=True)

# st.success('Model loaded successfully')
# st.success('Redis db successfully connected')



