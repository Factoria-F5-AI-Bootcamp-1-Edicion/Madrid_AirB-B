
#Importamos librerias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import pydeck as pdk
import numpy as np
from PIL import Image


#Creamos contenedores
header = st.container()
dataset = st.container()

#Sidebar

with st.sidebar: st.metric(label="Prices", value="70$ ", delta="1.2 $")


add_selectbox = st.sidebar.selectbox(
    " *Entrada",
    ("Pagina Principal", "Correlaciones", "Conclusiones")
)


#Dentro de la Pagina Principal

if add_selectbox== 'Pagina Principal':

    st.title("BIENVENIDO A MADRID!!! :tada: :smile:")
    st.markdown ('Creamos una herramienta de análisis de datos y predicción sobre conjuntos de datos de Airbnb.')
    image = Image.open('madrid.jpg')
    st.image(image, caption='Ciudad de Madrid')

    with dataset:
            
            st.title("Madrid Airbnb :hotel:")    
            madrid_data = pd.read_csv("madrid_airbnb.csv",)
        
            st.write(madrid_data.head(5))
            coordinates = madrid_data[["latitude", "longitude","price"]]
            price = madrid_data["price"]


        #Creamos botones en la pagina principal 
    page_names = [ ' *Datos', ' *Mapas']
    page = st.radio ('Navegamos',page_names)

    if page == ' *Datos':   
            plt.ion()
            plt.figure(figsize=(10,6))
            sns.scatterplot(x=madrid_data.longitude,y=madrid_data.latitude,hue=madrid_data.neighbourhood_group)

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
            else:
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
else:
    if add_selectbox== 'Correlaciones':
        st.title("Explorando Datos")

