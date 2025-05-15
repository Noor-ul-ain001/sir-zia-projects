import streamlit as st

# Set Page Configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
   page_icon="🧠", 
    layout="centered"
)

# Title and Subtitle
st.title("Unlock Your Growth Mindset 🧠")
st.subheader("Track your progress, analyze growth trends, and get instant guidance.")

# Add a Motivational Quote
st.markdown(
    "> *“Success is not an accident, success is a choice.”* – Stephen Curry"
)

# Display Sections with Buttons
st.write("### Explore the App:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📌 About Me"):
        st.switch_page("pages/about_me.py")

with col2:
    if st.button("📊 Sales Dashboard"):
        st.switch_page("pages/sale_dashboard.py")

with col3:
    if st.button("🤖 Chat Bot"):
        st.switch_page("pages/chatbot.py")

# Footer
st.markdown("---")
st.write("💡 Stay curious, keep growing, and challenge yourself every day!")

