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
if len(n) > 0:
    st.write(f"Hello {n}")


is_clicked = st.button("Click Me")

#st.image("finalPanda.png", caption=' ')


#st.write(f"Graph Test")
#data=pd.DataFrame(np.random.randn(20,3),
#                  columns=["a","b", "c"])
#st.bar_chart(data)
#st.line_chart(data)
#st.write(str(data))
scenario_title='<p style="font-family:Courier; color:Blue; font-size: 20px;">Scenario</p>'
st.write(scenario_title, unsafe_allow_html=True)
scenario="""Four college students from diverse racial backgrounds are interested in pursuing a career in international organizations. They are fortunate to land 
internships in an international company in Hong Kong. They all have high interest in learning Chinese language and culture and cybersecurity, and their job
 is to create materials that help increase cybersecurity awareness among the company's Chinese speaking employees worldwide. Through their collaboration, the interns skillfully crafted materials that not only addressed cybersecurity concerns but also resonated with the diverse linguistic and cultural backgrounds of 
the Chinese-speaking employees. Their efforts went beyond the technical realm, incorporating elements of storytelling, cultural sensitivity, and localized strategies to ensure the materials were not only informative but also engaging.
"""
st.write(scenario)
##    'Column 2': ['Freshman from Los Angela California; Ascian Studies major, extroverted; likes computer games; Desired work related to Asian Studies.',
##                 'Junior student from New York. Chinese major. Enjoys playing basketball and singing. Hopes to work in China in the future.',
##                 'Sophomore, from Denver, majoring in Software Engineering, third-generation Chinese immigrant, has some knowledge of Chinese culture, enjoys social media. Hope to work as a software engineer in the future.',
##                 'Junior student, from Houston. Cybersecurity major, enjoys cooking and traveling. Hope to work in cybersecurity in the future.']
## 
data = {

    'Column 1': ['Melissa 周萌', 'Jaden 王杰丹', 'Mei  李梅', 'Diego 张笛'],
    'Column 2': ['Freshman from Los Angela California; Asian Studies major',
                 'Junior student from New York. Chinese major. Enjoys playing basketball and singing. Hopes to work in China in the future.',
                 'Sophomore, from Denver, majoring in Software Engineering, third-generation Chinese immigrant, ',
                 'Junior student, from Houston. Cybersecurity major, enjoys cooking and traveling. Hope to work in cybersecurity in the future.'],
     'Column 3': ['panda.png', 'panda.png', 'panda.png', 'panda.png']
}
df = pd.DataFrame(data)
# Define CSS style for the table
##table_style = """
##    <style>
##        table {
##            border-collapse: collapse;
##        }
##        th, td {
##            border: 1px solid black;
##            padding: 8px;
##            text-align: left;
##        }
##    </style>
##"""
##
### Display the HTML table with borders
##st.write(table_style, unsafe_allow_html=True)
##st.write(df)

# Display the table with borders
##st.markdown(
##    df.style.set_properties(**{'border': '1px solid black', 'border-collapse': 'collapse'}).render(), 
##    unsafe_allow_html=True
##)
# Display the table with images
for index, row in df.iterrows():
    col1, col2, col3 = st.columns([1, 3, 1])  # Define column widths
    with col1:
        st.write(f"**{row['Column 1']}**")
    with col2:
        st.write(row['Column 2'])
    with col3:
        st.image(row['Column 3'], width=200, caption=row['Column 1'])
##
