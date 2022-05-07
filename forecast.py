import streamlit as st
import pandas as pd
import numpy as np


def app():
    st.title("Forecasting of Various Crimes in India (District Wise)")
    df = pd.read_csv("District_Crime_Till_2013.csv")

    district = list(df.DISTRICT.value_counts().index)

    res = {}
    cols = list(set(df.columns) - {'Unnamed:0', "STATE/UT", "DISTRICT"})
    for i in district:
        res[i] = pd.DataFrame(df[df["DISTRICT"] == i][cols]).reset_index()
        res[i].drop(columns="index", inplace=True)
    st.subheader("Select the District")
    optiond = st.selectbox("select",list(df["DISTRICT"].value_counts().index))
    st.subheader("Select the Crime to explore about the forecast!!")
    crimes = tuple(set(df.columns)-{'YEAR','STATE/UT','DISTRICT','Unnamed:0'})
    optionc = st.selectbox("",crimes)
    if optiond and optionc:
        import matplotlib.pyplot as plt
        import numpy as np
        res[optiond]["Forecast"] = np.array(res[optiond][optionc].rolling(window=3).mean())

        arr = pd.Series(list(res[optiond]["Forecast"]),index=list(res[optiond]["YEAR"]))
        fig, ax = plt.subplots()
        ax.plot(arr)

        st.pyplot(fig)
        #print(len(list(res[optiond]["YEAR"])),)
        #print(len(list(res[optiond]["Forecast"])))
        st.line_chart(list(res[optiond]["YEAR"]), )
        #fig = plt.plot(res[optiond]["YEAR"], res[optiond]["Forecast"])
        #st.line_chart(res[optiond]["YEAR"], res[optiond]["Forecast"])



