import Travel_Safety
import Crime_Analysis
import Travel_Route
import forecast
import Report
import streamlit as st
PAGES = {
    "Travel Safety": Travel_Safety,
    "Crime Analysis": Crime_Analysis,
    "Optimal Travel Route": Travel_Route,
    "Forecasting of Crime": forecast,
    "Report a Crime":Report
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()