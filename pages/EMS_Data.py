import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMS Data Dashboard")

data = pd.read_csv("ems_data.csv")

statezz = data["State"].unique()
selected = st.selectbox("Pick a State (or not)", statezz)

incidentzz = data["IncidentType"].unique()
chosen_incident = st.selectbox("Pick the emergency flavor", incidentzz)

pls_work = data[(data["State"] == selected) & (data["IncidentType"] == chosen_incident)]

if not pls_work.empty:
    time_thing = pls_work["ResponseTime"].values[0]
    amount_of_panic = pls_work["CallCount"].values[0]

    st.subheader("The Stats You Probably Wanted")
    st.write("Average response time:", time_thing, "minutes")
    st.write("Number of calls handled:", amount_of_panic)

    fig, ax = plt.subplots()
    ax.bar(["Speed", "Calls"], [time_thing, amount_of_panic], color="green")
    ax.set_title(f"{chosen_incident} in {selected}")
    st.pyplot(fig)
else:
    st.warning("Nothing to see here")
