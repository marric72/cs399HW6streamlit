import streamlit as st
import pandas as pd
import numpy as np
import base64

title = '<p style="font-family:Courier; color:Blue; font-size: 30px;">Episode 1</p>'
st.markdown(title, unsafe_allow_html=True)

audio_file = open('file.mp3', 'rb')
audio_bytes = audio_file.read()

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    #pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


# Streamlit app
def main():
    st.title("Conversation with Melissa and Doug")
    st.image("panda.png", caption=' ')
    
    # Button to show WeChat
    if st.button("See WeChat Transcript"):
        st.markdown(weChat, unsafe_allow_html=True)

    # Button to see vocab pdf
    if st.button("See Unit1 Vocabulary"):
        displayPDF("vocab_unit1_1.pdf")
    # Button to trigger playing the MP3 file
    if st.button("See Conversation Between Melissa and Doug"):
        #audio_file = open('file.mp3', 'rb')
        #audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mpeg')

    weChat="""Unit 1 Part I: Self-introduction WeChat Posts 

周萌的自我介绍 

你好，我姓周，叫周萌。我是大一的学生，我的专业是亚洲研究。我是加州人， 喜欢玩电脑 游戏。   我希望将来做亚洲研究工作。　                              

                       

王杰丹的自我介绍 

大家好！我姓王，叫王杰丹。我是大三的学生，我的专业是 

中文。我是纽约人，很喜欢打篮球，也喜欢唱歌。我希望将来在中国工作。　 

 

李梅的自我介绍 

你好！我姓李，叫李梅。 我是大二的学生，我的专业是软件工程。我是丹佛人，喜欢社交媒体。我希望将来做软件工程师的工作。 

 

张笛的自我介绍 

你好！我姓张，叫张笛。我也是大三的学生。我的专业是网络安全。我是休斯顿人，我喜欢做饭和旅行。我希望将来做网络安全工作。 """

 



if __name__ == "__main__":
    main()

