import google.generativeai as genai
import streamlit as st
import re

GOOGLE_API_KEY = "AIzaSyA07EFG1ki9z1qA8U5mBt_I4hqeu3Oyz2M"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    clean_response = response.text.lstrip('#').strip()
    return clean_response

st.set_page_config(page_title="Punisher's Chatbot", layout="wide")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    input {
        background-color: #333333;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Punisher's Chatbot")
st.write("Made by Ehtisham")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:", max_chars=2000, label_visibility="hidden")
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})

            response = getResponseFromModel(user_input)

            st.session_state.messages.append({"role": "bot", "content": response})

            st.markdown(
                f'<div style="text-align: right; background-color: #1e1e1e; border-radius: 10px; padding: 10px; margin: 5px; color: #FFFFFF;"><b>You:</b> {user_input}</div>', 
                unsafe_allow_html=True
            )
            st.markdown(
                f'<div style="text-align: left; background-color: #2e2e2e; border-radius: 10px; padding: 10px; margin: 5px; color: #FFFFFF;">{response}</div>', 
                unsafe_allow_html=True
            )
            for message in st.session_state.messages[:-2]:
                if message["role"] == "user":
                    st.markdown(
                        f'<div style="text-align: right; background-color: #1e1e1e; border-radius: 10px; padding: 10px; margin: 5px; color: #FFFFFF;"><b>You:</b> {message["content"]}</div>', 
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f'<div style="text-align: left; background-color: #2e2e2e; border-radius: 10px; padding: 10px; margin: 5px; color: #FFFFFF;">{message["content"]}</div>', 
                        unsafe_allow_html=True
                    )
            st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)
        else:
            st.warning("Please Enter a Prompt.")