import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini + Streamlit Demo", page_icon="🤖")
st.title("🤖 Gemini AI Chat – Streamlit Example")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask Gemini anything...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    response = model.generate_content(prompt)
    reply = response.text

    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
