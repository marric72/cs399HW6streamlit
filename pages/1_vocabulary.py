import streamlit as st
import pandas as pd

st.write("Vocabulary Lesson 1")
data = pd.read_csv("CurriculumMap.csv")
st.write(data)
