import streamlit as st
import pandas as pd
import pydeck as pdk   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_option_menu import option_menu

#Se quita aviso de pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
#NavBar
    selected = option_menu( "Home Madrid", ["Home", "Datos", "Outliers", "Contacto"],
        icons=["house", "geo-alt", "graph-up","chevron-bar-expand", "chat"],  # optional
        menu_icon="cast",  # optional
        default_index=0)

   # st.metric(label="Prices", value="70$ ", delta="1.2 $")



data = pd.read_csv("madrid_airbnb.csv")

if selected == "Home":

    st.title("Bienvenido a Madrid :smile:")

    st.image("madrid.jpg")

    box= st.sidebar.selectbox("Descubre",["Distritos","Anuncios"],index=0)
    if box== "Distritos":
        st.subheader("Podemos observar los distritos de Madrid: ")
        plt.ion()
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=data.longitude,y=data.latitude,hue=data.neighbourhood_group)
        st.pyplot()
        
        

if selected== "Datos":

    st.header("Base de datos Madrid Airbnb:")

#Vizualizacion de la Base de Datos
    st.markdown("Se puede mostrar parte de la base datos para su visualizacion: ")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.write(data.head(20))
    
#Visualizacion de los distritos degun su precio
    st.subheader("Distritos segun su precio:")
    plt.scatter(data["price"],data["neighbourhood_group"])
    plt.title("Scatter Plot")
    st.pyplot()

#Se crea boton para visualizar mapa segun precio
    if st.button ('Mapa segun precio'):
                coordinates= data[["latitude","longitude","price"]]    

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
#Visualizacion de los distritos degun su cantidad de anuncios

    st.subheader("Distritos segun su cantidad de anuncios:")
    st.bar_chart((data['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count" )
#Se crea boton para visualizar mapa segun su cantidad de anuncios

    if st.button ('Mapa segun anuncio'):

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
            ],
        ))

#Visualizacion de los hospedajes segun su precio
    st.subheader("Tipo de hospedaje segun su precio:")
    plt.scatter(data["room_type"],data["price"])
    plt.title("Scatter Plot")
    st.pyplot()
    

if selected== "Outliers":

    st.title ("Mapas segun relacion")
