import streamlit as st
import pandas as pd
import pydeck as pdk   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


rad = st.sidebar.radio("Navega",["Conoce Madrid","Nuestro datos","Mapa Densidad", "Mapa Precios"])
data = pd.read_csv("madrid_airbnb.csv")

if rad== "Conoce Madrid":

    st.title("Bienvenido a Madrid :)")

    st.image("FotoMadrid.jpg")

    box= st.sidebar.selectbox("Descubre",["Distritos","Anuncios"],index=0)
    if box== "Distritos":
        plt.ion()
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=data.longitude,y=data.latitude,hue=data.neighbourhood_group)
        st.pyplot()
    if box=="Anuncios":
        st.bar_chart((data['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count" )


   
    
if rad== "Nuestro datos":
    
    st.video("https://www.youtube.com/watch?v=-Xv5rw_Xv8c")
    
    plt.scatter(data["price"],data["neighbourhood_group"])
    
    plt.title("Scatter Plot")
    
    st.pyplot()

    champions = data.groupby("neighbourhood_group").mean()

    champions['price'].plot(kind = 'bar')
    st.pyplot() 

    
 
if rad== "Mapa Densidad":

    coordinates= data[["latitude","longitude","price"]]

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

if rad== "Mapa Precios":

    coordinates= data[["latitude","longitude","price"]]

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




