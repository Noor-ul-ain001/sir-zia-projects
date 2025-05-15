import streamlit as st

st.title("🤖 Chat Bot")
st.write("Ask me anything about growth mindset strategies!")

# Simulated Chatbot
user_input = st.text_input("Ask a question:")
if user_input:
    st.write(f"🔹 **Chatbot:** Stay consistent and keep learning, {user_input}!")
