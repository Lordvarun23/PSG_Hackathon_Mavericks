import streamlit as st
import folium
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium
import geopy.distance

def app():
    st.title("Optimal Travel Route")
    st.markdown("Based on the given To and From locations. It suggests the best route along with all the other neccessary details.")
    st.text_input("From: DISTRICT", key="from_district")
    st.text_input("To: DISTRICT", key="to_district")

    geolocator = Nominatim(user_agent="my_user_agent")
    city = st.session_state.to_district
    country = "India"
    loc1 = geolocator.geocode(city + ',' + country)
    loc2 = geolocator.geocode(st.session_state.from_district + ',' + country)

    df = {'lat':[loc1.latitude,loc2.latitude], 'long':[loc1.longitude,loc2.longitude]}
    if st.session_state.to_district:
        st.text("The Distance Between the given two locations is: " + str(round(geopy.distance.geodesic([loc1.latitude,loc1.longitude],[loc2.latitude,loc2.longitude]).km,3))+"KM")
        m = folium.Map(location=[loc2.latitude,loc2.longitude+0.01], zoom_start=26)
        folium.Marker(
            [loc1.latitude,loc1.longitude],
            popup=st.session_state.from_district,
            tooltip=st.session_state.from_district
        ).add_to(m)
        folium.Marker(
            [loc2.latitude,loc2.longitude],
            popup=st.session_state.to_district,
            tooltip=st.session_state.to_district
        ).add_to(m)
        loc = [(loc1.latitude, loc1.longitude), (loc2.latitude, loc2.longitude)]
        folium.PolyLine(loc,
                        color='red',
                        weight=15,
                        opacity=0.8).add_to(m)

        # call to render Folium map in Streamlit
        st_data = st_folium(m, width=725)

'''
folium.PolyLine(loc,
                        color='red',
                        weight=15,
                        opacity=0.8).add_to(m)'''

