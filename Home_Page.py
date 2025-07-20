import streamlit as st

st.title("EMS Response Analyzer")
st.subheader("CS 1301 ")
st.subheader("Fatih Ozel")

st.write("""
Welcome to our Streamlit Web Development Lab02 app! You can navigate between the pages using the sidebar. The following pages are:

1. **EMS_Data**: Visualizes EMS data with interactive charts based on selected state and incident type.
2. **EMS_Report**: Uses Google Gemini to generate a written summary from the selected EMS data.
3. **EMS_Chatbot**: Allows users to ask questions about EMS response systems, answered by an AI-powered chatbot.
""")

