import streamlit as st
from PIL import Image


# 画像
image = Image.open('./data/唐揚げリサイズA3.jpg')
st.image(image)
