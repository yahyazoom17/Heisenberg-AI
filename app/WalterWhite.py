import streamlit as st
import ai

st.set_page_config(page_title="Walter White(Breaking Bad)", layout="centered")

# --- Session state to store chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Chat message renderer ---
def display_chat():
    for role, message in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"<div style='background-color: green; color: white; padding: 5px; border-radius: 5px; margin: 5px; font-size: 18px;'><span style='margin: 10px;'>{message}</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: white; color: black; padding: 5px; border-radius: 5px; margin: 5px;'><span style='margin: 20x;'>{message}</span></div>", unsafe_allow_html=True)

# --- Title and Chatbox ---
st.title("🧑 Heisenberg AI")

# --- Input box ---
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message...", "")
    submit_button = st.form_submit_button(label="Send")

# --- Process input ---
if submit_button and user_input.strip():
    st.session_state.chat_history.append(("user", user_input))

    # Simulated bot response (replace with your AI backend logic)
    bot_response = ai.askWalt(user_input)
    st.session_state.chat_history.append(("bot", bot_response))

    #Rerun to display chats
    st.rerun()

with st.container():
    display_chat()

st.image("../assets/heisenberg-ai-logo.svg", caption="Created By Yahya", use_container_width=True)