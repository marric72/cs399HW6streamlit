import streamlit as st
import pandas as pd
import numpy as np

#Write text to the screen
original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Red; font-size: 30px;">Original image</p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
n=st.text_input("Enter name")
st.write(f"Hello {n}")


is_clicked = st.button("Click Me")

st.image("cat.png", caption='my cat Sunshine')


st.write(f"Graph Test")
data=pd.DataFrame(np.random.randn(20,3),
                  columns=["a","b", "c"])
st.bar_chart(data)
st.line_chart(data)
st.write(str(data))
