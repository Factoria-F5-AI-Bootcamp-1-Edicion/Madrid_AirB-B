
from asyncore import write
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

#Variables
madrid_data = pd.read_csv("madrid_airbnb.csv",)
coordinates = madrid_data[["latitude", "longitude", "price"]]
price = madrid_data["price"]

#Containers
header = st.container()
body = st.container()
sidebar = st.container()



# Using "with" notation

with header:
    
   
    
    st.title("BIENVENIDO A MADRID!!! :tada: :smile:")

with body:

    st.title("Madrid Airbnb :hotel:")


    st.write(madrid_data.head(50))
    
    
    st.write(price.head(50))


#Sidebar

with st.sidebar:

#NavBar
    selected = option_menu(
    menu_title="Home Madrid",  # required
    options=["Home", "Datos", "Outliers", "Contacto"],  # required
    #icons=["house", "geo-alt", "graph-up","chevron-bar-expand", "chat"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    
            )
    st.metric(label="Prices", value="70$ ", delta="1.2 $")

    add_selectbox = st.sidebar.selectbox(
    "Years",
    ("2019", "2020", "2021")
)

with st.sidebar:
    map_type = st.radio(
        "Choose a map type",
        ("Density", "Columns")
        )

    if map_type == "Density":
        st.write("heatmap")
    
    else:
        with dataset:
            st.write(coordinates.head(50))




# Map 1
heatmap = st.pydeck_chart(pdk.Deck(

    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=40.41596,
        longitude=-3.7325,
        zoom=11,
        pitch=50,
    ),
    
    layers=[
        pdk.Layer(
            'HeatmapLayer',
            data=coordinates,
            get_position='[longitude, latitude]',
            radius=5,
            elevation_scale=1,
            elevation_range=[0, 500],
            pickable=True,
            extruded=True,




        ),
        #  pdk.Layer(
        #      'ScatterplotLayer',
        #      data = coordinates,
        #      get_position='[longitude, latitude]',
        #      get_color='[200, 30, 0, 160]',
        #      get_radius=5,
        #  ),
    ],
))

# Map 2


tooltip = {
    "html": "Cost <strong>{price}$</strong>",
}

columns_map = st.pydeck_chart(pdk.Deck(
    map_style=None,
    tooltip=tooltip,
    initial_view_state=pdk.ViewState(
        latitude=40.41596,
        longitude=-3.7325,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ColumnLayer',
            data=coordinates,
            get_position='[longitude, latitude]',
            radius=10,
            elevation_scale=0.25,
            elevation_range=[0, 1000],
            get_elevation='[price]',
            pickable=True,
            extruded=True,
            


            getFillColor=[150, 3, 0, 255]




        ),

    ],
))


    