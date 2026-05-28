import requests
import streamlit as st

st.title("FastAPI Text to Image")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.image(message["content"])

if prompt := st.chat_input("Write your prompt in this input field"):
    st.session_state.messages.append({"role":"user", "content": prompt})

    with st.chat_message("user"):
        st.text(prompt)

    response = requests.get(
        f"http://127.0.0.1:8000/generate/images", params = {"prompt":prompt}
    )

    response.raise_for_status()
    
    with st.chat_message("assistant"):
        st.text("Here is your generated image")
        st.image(response.content)