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

# User inputs

## Func for taking user inputs

def get_text():
    input_text = st.text_input("Prompt me something, please ", "", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_text()

# Bot outputs


## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    response = chatbot.chat(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state['generated'][i], key=str(i))



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)









































