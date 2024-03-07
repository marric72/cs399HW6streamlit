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

# Display radio buttons for toggling between two choices
selection = st.radio("Choose one:", ["Student", "Educator"])
if selection == "Student":
        # Display the selected option
        #st.write("You selected:", selection)

        #write user input to screen
        n=st.text_input("Enter name")
        if len(n) > 0:
                title = f'<p style="font-family:Courier; color:Blue; font-size: 20px;">Welcome {n}</p>'
                st.markdown(title, unsafe_allow_html=True)


        # Add a blank line
        st.write("")

        # Add a horizontal line
        #st.markdown("<hr>", unsafe_allow_html=True)

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


        ep1b="""1. Able to introduce oneself including basic information about name, grade year, major, hometown, likes, and future career. <br><br>2. Able to ask others about name, grade, major, homework, likes, and future career, and nationalities. <br><br>3. Make suggestion to do something together."""

        data = [
            ['Episode 1: The Dream Begins', ep1, ep1b],
            ['Episode 2: Orientation Day', "", ""],
            ['Episode 3: Kick off Meeting', "", ""],
            ['Episode 4: Job Training', "", ""]
        ]
        headers = ["Episodes",
                   "<div style='text-align: center'>Storyline</div>",
                   "<div style='text-align: center'>Learning Outcomes</div>"]  # Include header for the third column

        df = pd.DataFrame(data, columns=headers)

        # Generate HTML markup for the table
        html_table = df.to_html(index=False, escape=False)



        # Display the table with custom CSS
        st.write(html_table, unsafe_allow_html=True)
        #st.markdown(custom_css, unsafe_allow_html=True)
else:
        st.write("show different stuff")
