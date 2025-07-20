import streamlit as st
import pandas as pd
import google.generativeai as genai

st.title("AI Report Generator")

data = pd.read_csv("ems_data.csv")

where = data["State"].unique()
which_state = st.selectbox("Choose a state I guess", where)

what = data["IncidentType"].unique()
which_incident = st.selectbox("What kind of emergency are we talking", what)

filtered = data[(data["State"] == which_state) & (data["IncidentType"] == which_incident)]

if not filtered.empty:
    speed = filtered["ResponseTime"].values[0]
    calls = filtered["CallCount"].values[0]

    prompt = f"""
    make a nice summary about this
    state: {which_state}
    incident: {which_incident}
    response time: {speed}
    calls: {calls}
    """

    genai.configure(api_key="AIzaSyCEhsLFYdEdq2FcYgf_rTNrrOyjBgv2Ka4")
    model = genai.GenerativeModel("gemini-2.5-pro")
    chat = model.start_chat()

    try:
        result = chat.send_message(prompt)
        st.subheader("Gemini Said This")
        st.write(result.text)
    except Exception as whatever:
        st.error("something went wrong, not my fault")
else:
    st.warning("not enough data to do anything")


