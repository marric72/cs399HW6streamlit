import streamlit as st
import pandas as pd
import numpy as np



#Write text to the screen
#original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Original image</p>'
#st.markdown(original_title, unsafe_allow_html=True)

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">Episode 1</p>'
st.markdown(title, unsafe_allow_html=True)

#write user input to screen
#n=st.text_input("Enter name")
#if len(n) > 0:
#    st.write(f"Hello {n}")


#is_clicked = st.button("Click Me")

st.image("panda.png", caption=' ')


#st.write(f"Graph Test")
#data=pd.DataFrame(np.random.randn(20,3),
#                  columns=["a","b", "c"])
#st.bar_chart(data)
#st.line_chart(data)
#st.write(str(data))
#scenario_title='<p style="font-family:Courier; color:Blue; font-size: 20px;">Scenario</p>'
#st.write(scenario_title, unsafe_allow_html=True)

import streamlit as st

# Function to generate HTML code for playing audio
def generate_audio_html(audio_file, caption):
    audio_html = f'''
    <audio controls>
        <source src="{audio_file}" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
    <p>{caption}</p>
    '''
    return audio_html

# Streamlit app
def main():
    st.title("Conversation with Melissa and Doug")

    # Button to trigger playing the MP3 file
    if st.button("Play"):
        #playsound("chatMelissaAndDoug.mp3") 
        #audio_file = "chatMelissaAndDoug.mp3"  # Replace with the path to your MP3 file
        #caption = "Your MP3 is playing!"
        #audio_html = generate_audio_html(audio_file, caption)
        #st.markdown(audio_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

