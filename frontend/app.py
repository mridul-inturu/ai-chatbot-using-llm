import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_input}
    )

    data = response.json()

    if "reply" in data:
        reply = data["reply"]
    else:
        reply = f"Backend error: {data}"

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", reply))

for sender, message in st.session_state.chat_history:
    st.write(f"**{sender}:** {message}")
