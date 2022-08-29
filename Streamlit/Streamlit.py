import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

st.title('Madrid Air BnB')

page_names = [ 'Datos', 'Mapas']
page = st.radio ('Navegamos',page_names)

if page == 'Datos':

    st.subheader ("Madrid Airbnb :hotel:")    
    madrid_data = pd.read_csv("madrid_airbnb.csv",)
    coordinates = madrid_data[["latitude", "longitude","price"]]
    price = madrid_data["price"]
   
    st.write(madrid_data.head(10))

else :
    option = st.selectbox(
     'Elige que tipo de mapa quieres ver: ',
     ('Heatmap', 'Scatterplot'))

    st.write('You selected:', option)

    if option == 'Heatmap':

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
            madrid_data = pd.read_csv("madrid_airbnb.csv",),
            coordinates = madrid_data[["latitude", "longitude","price"]],
            price = madrid_data["price"],
            data= coordinates,
            get_position='[longitude, latitude]',
            radius=5,
            elevation_scale=1,
            elevation_range=[0, 500],
            pickable=True,
            extruded=True,
            
),
        
     ],
 ))