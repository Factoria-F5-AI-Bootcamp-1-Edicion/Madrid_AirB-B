
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np


st.set_page_config(layout="wide")


header = st.container()
dataset = st.container()

#Sidebar
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
with st.sidebar: st.metric(label="Temperature", value="70 °F", delta="1.2 °F")



with header:
    st.title("BIENVENIDO A MADRID!!! :tada: :smile:")

with dataset:
    
    st.title("Madrid Airbnb :hotel:")    
    madrid_data = pd.read_csv("madrid_airbnb.csv",)
   
    st.write(madrid_data.head(50))
    coordinates = madrid_data[["latitude", "longitude"]]
    st.write(coordinates.head(50))


    st.map (coordinates,)

st.pydeck_chart(pdk.Deck(
     map_style=None,
     initial_view_state=pdk.ViewState(
         latitude=37.76,
         longitude=-122.4,
         zoom=11,
         pitch=50,
     ),
     layers=[
         pdk.Layer(
            'HexagonLayer',
            data=coordinates,
            get_position='[longitude, latitude]',
            radius=10,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
         ),
         pdk.Layer(
             'ScatterplotLayer',
             data=coordinates   ,
             get_position='[longitude, latitude]',
             get_color='[200, 30, 0, 160]',
             get_radius=10,
         ),
     ],
 ))