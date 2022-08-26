
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np


st.set_page_config(layout="wide")


header = st.container()
dataset = st.container()

#Sidebar
add_selectbox = st.sidebar.selectbox(
    "Years",
    ("2019", "2020", "2021")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Heatmap", "Columns")
    )
with st.sidebar: st.metric(label="Prices", value="70$ ", delta="1.2 $")



with header:
    st.title("BIENVENIDO A MADRID!!! :tada: :smile:")

with dataset:
    
    st.title("Madrid Airbnb :hotel:")    
    madrid_data = pd.read_csv("madrid_airbnb.csv",)
   
    st.write(madrid_data.head(50))
    coordinates = madrid_data[["latitude", "longitude","price"]]
    price = madrid_data["price"]
    st.write(coordinates.head(50))
    st.write(price.head(50))


    
#Map 1
st.pydeck_chart(pdk.Deck(
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
            data= coordinates,
            get_position='[longitude, latitude]',
            radius=5,
            elevation_scale=1,
            elevation_range=[0, 500],
            pickable=True,
            extruded=True,
            
    
        

         ),
         pdk.Layer(
             'ScatterplotLayer',
             data = coordinates,
             get_position='[longitude, latitude]',
             get_color='[200, 30, 0, 160]',
             get_radius=5,
         ),
     ],
 ))

 #Map 2

st.pydeck_chart(pdk.Deck(
     map_style=None,
     initial_view_state=pdk.ViewState(
         latitude=40.41596,
         longitude=-3.7325,
         zoom=11,
         pitch=50,
    
     ),
     layers=[
         pdk.Layer(
            'ColumnLayer',
            data= coordinates,
            get_position='[longitude, latitude]',
            radius=10,
            elevation_scale=0.25,
            elevation_range=[0, 1000],
            get_elevation = '[price]',
            pickable=True,
            extruded= True,
            getTooltip='[price]',
            
            
            getFillColor= [150, 3, 0, 255]
            
    
        

         ),
        
     ],
 ))

