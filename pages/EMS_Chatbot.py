import streamlit as st
import google.generativeai as genai

st.title("Emergency Chatbot")

genai.configure(api_key="AIzaSyCEhsLFYdEdq2FcYgf_rTNrrOyjBgv2Ka4")
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()

if "memory_dump" not in st.session_state:
    st.session_state.memory_dump = []

thing_to_ask = st.text_input("Type something about EMS or whatever")

if thing_to_ask:
    st.session_state.memory_dump.append(("You", thing_to_ask))

    try:
        reply = chat.send_message(thing_to_ask)
        st.session_state.memory_dump.append(("Chatboy", reply.text))
    except:
        st.session_state.memory_dump.append(("Chatboy", "I crashed again but it's fine"))

for speaker, words in st.session_state.memory_dump:
    st.write(speaker + ": " + words)

