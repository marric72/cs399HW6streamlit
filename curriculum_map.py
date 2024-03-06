import streamlit as st
import pandas as pd
import numpy as np

#Write text to the screen
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
#st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">CYBOT - Cyber/Computer Online Training</p>'
st.markdown(title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:White; font-size: 20px;">Interactive Website for Cyber Chinese Curriculum</p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
n=st.text_input("Enter name")
if len(n) > 0:
	title = f'<p style="font-family:Courier; color:Blue; font-size: 20px;">Welcome {n}</p>'
	st.markdown(title, unsafe_allow_html=True)


#is_clicked = st.button("Click Me")

#st.image("finalPanda.png", caption=' ')
data = {
        'Column 1': ['Episodes',
                 'Episode 1: The Dream Begins',
                 'Episode 2: Orientation Day',
                 'Episode 3: Kick off Meeting',
                 'Episode 4: Job Training'],
        'Column 2': ['Storyline',
                 '• Melisa, Jaden, Mei, and Diego received an acceptance letter for a cybersecurity internship from an International Company in Hong Kong. The internship program director Lily created a WeChat Group and each of interns posted a self-introduction to the group chat.',
                 '•  They all share their passion for cybersecurity and their interest in learning the Chinese language and culture. They also are excited to meet with other interns.',
                 '  ghj',
                 '  ghj '],
        'Column 3': ['Melissa.png', 'Jade.png', 'Mei.png', 'Diego.png','Diego.png']
}
# Display the table

#df = pd.DataFrame(data)

def display_table(data, headers):
    # Calculate the maximum width of each column
    col_widths = [max(len(str(row[i])) for row in data) for i in range(len(headers))]
    
    # Print the header row
    header_row = " | ".join(headers)
    print(header_row)
    
    # Print a separator line
    separator = "+".join("-" * width for width in col_widths)
    print(separator)
    
    # Print the data rows
    for row in data:
        formatted_row = " | ".join(str(value).ljust(width) for value, width in zip(row, col_widths))
        print(formatted_row)

# Sample data

import streamlit as st
import pandas as pd

ep1 = """• Mellisa, Jaden, Mei, and Diego received an acceptance letter for a cyber security internship from an International Company in Hong Kong. The internship program director Lily created a WeChat Group and each of interns posted a self-introduction to the group chat.<br><br>• They all share their passion for cybersecurity and their interest in learning Chinese language and culture. They also are excited to meet with other interns."""

data = [
    ['Episode 1: The Dream Begins', ep1, "", "", ""],
    ['Episode 2: Orientation Day', 30, "", "", ""],
    ['Episode 3: Kick off Meeting', 35, "", "", ""],
    ['Episode 4: Job Training', 35, "", "", ""]
]
headers = [" ", "Episodes",
           "<div style='text-align: center'>Storyline</div>", "Learning Outcomes", "Topics and Subtopics"]
df = pd.DataFrame(data, columns=headers)

# Generate HTML markup for the table
html_table = df.to_html(index=False, escape=False)

# Apply custom CSS to hide row numbers
custom_css = """
<style>
/* Hide row numbers */
table.dataframe tr th:first-child {
    display: none;
}
</style>
"""

# Display the table with custom CSS
st.write(html_table, unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)
