import streamlit as st
import pandas as pd


def app():
    st.title("Travel Safety")
    st.markdown(" We have collected the data of all previous committed crimes in various districts of India. Our Idea is to help the people to make wise decisions and to know more about the place they are travelling to.\n\n So all you have to do is to enter the To and Fro details and Our application will give you a brief picture about destination.")
    df = pd.read_csv("District_Crime_Till_2013.csv")

    district = list(df.DISTRICT.value_counts().index)

    res = {}
    cols = list(set(df.columns) - {'Unnamed:0', "STATE/UT", "DISTRICT"})
    for i in district:
        res[i] = pd.DataFrame(df[df["DISTRICT"] == i][cols]).reset_index()
        res[i].drop(columns="index", inplace=True)
    try:
        st.text_input("From: STATE", key="from_state")
        st.text_input("From: DISTRICT", key="from_district")
        st.text_input("To: STATE", key="to_state")
        st.text_input("To: DISTRICT", key="to_district")

        option = st.selectbox(
            'Gender',
            ('Male', 'Female', 'Prefer not to say'))

        option1 = st.selectbox(
            'Do you want a list of all crime that are higher in your destination from your current place?',
            ('No', 'Yes'))
        # You can access the value at any point with:
        col = list(set(df.columns) - {'Unnamed:0', "STATE/UT", "DISTRICT", "YEAR"})
        count = 0
        if st.session_state.to_district in res and st.session_state.from_district in res:
            for i in col:
                if float(res[str(st.session_state.from_district)][i][-1:]) > float(
                        res[str(st.session_state.to_district)][i][-1:]):
                    count += 1
                else:
                    if option1 == "Yes":
                        st.text("The City " + st.session_state.to_district + " Has high rate of " + i)
                    else:
                        continue

            if count > len(col) / 2:
                st.text("The going City is safer than the present city!!")
            else:
                if option=='Female':
                    st.text('''Don’t take eve teasing lightly\n

a.       Respond with a stern voice\n

b.      Threaten to take a picture which might scare them away\n

c.       If the eve teasing still persists then immediately raise your voice to gather a crowd\n

4.       As much as possible avoid late night travel using public transport\n
\n
a.       If avoiding is not possible then be sure to travel only on crowded bus
\n
b.      Avoid taking road side cabs
\n
c.       Avoid using a bus which has no passenger or few passenger
\n
5.       While using 2 wheeler be sure to wear helmet at all times (especially at night). Don’t stop for any stranger
\n
a.       In case attacked, use your helmet to defend yourself''')


        else:
            st.text("The Details of the given city is unavailable. Please check back later!!")
    except ValueError:
        st.error("Please enter a valid input")
