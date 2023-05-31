#Author Tushar Aggarwal(https://www.tushar-aggarwal.com/)

# Impoting the required libraries
import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
# Page Configration
# Application title and body
st.set_page_config(page_title="🤖T-BOT🤖",
                   page_icon="🤖",
                   layout='wide')
# Title of application
st.title("🤖T-BOT🤖 with HugChat")
st.markdown("### By [Tushar Aggarwal](https://www.tushar-aggarwal.com/)")

# Page Structure
with st.sidebar:
    st.title("🤗HugChat App🤗")
    st.markdown('''
        ### 
    By [Tushar Aggarwal](https://www.tushar-aggarwal.com/)

    🤗 Note: No API key required, Enjoy!🤗
    ''')

# Session State
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["Hi, I'm T-BOT, How may i help you today?"]
if 'past' not in st.session_state:
    st.session_state['past']= ['Hi!']

# Application layout
 

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

































# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)









































