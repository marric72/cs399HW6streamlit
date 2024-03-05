import streamlit as st
import pandas as pd
import numpy as np

#Write text to the screen
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
#st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CYBOT - Cyber/Computer Online Training</p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
n=st.text_input("Enter name")
st.write(f"Hello {n}")


is_clicked = st.button("Click Me")

st.image("finalPanda.png", caption=' ')


#st.write(f"Graph Test")
#data=pd.DataFrame(np.random.randn(20,3),
                  columns=["a","b", "c"])
#st.bar_chart(data)
#st.line_chart(data)
#st.write(str(data))
scenario_title='<p style="font-family:Courier; color:Blue; font-size: 20px;">Scenario</p>'
st.write(scenario_title, unsafe_allow_html=True)
st.write("Four college students from diverse racial backgrounds are interested in pursuing a career in international organizations. They are fortunate to land 
internships in an international company in Hong Kong. They all have high interest in learning Chinese language and culture and cybersecurity, and their job is 
to create materials that help increase cybersecurity awareness among the company's Chinese speaking employees worldwide. Through their collaboration, the 
interns skillfully crafted materials that not only addressed cybersecurity concerns but also resonated with the diverse linguistic and cultural backgrounds of 
the Chinese-speaking employees. Their efforts went beyond the technical realm, incorporating elements of storytelling, cultural sensitivity, and localized 
strategies to ensure the materials were not only informative but also engaging.")                                     
