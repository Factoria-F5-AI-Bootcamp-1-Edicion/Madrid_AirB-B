import streamlit as st
import pandas as pd
import pydeck as pdk   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#Desde aqui va la parte de Rebeca
rad = st.sidebar.radio("Navega",["HOME","Nuestro datos","Mapa Densidad", "Mapa Precios"])
data = pd.read_csv("madrid_airbnb.csv")

if rad== "HOME":

    box= st.sidebar.selectbox(" ",["Conoce Data Home","Descubre Madrid"],index=0)

    if box== "Conoce Data Home":

        st.title("Data Home Madrid") 
        
        st.write("Somos una empresa de consultoría de nueva generación especializada en hostelería y turismo, basada en análisis de datos e Inteligencia Artifical")
        
        st.image("Roof & casa.jpg")
        
        
        st.subheader("**Transformamos los datos en valor y utilidad para tu negocio**")

        st.image("FotoMadrid.jpg")
        
        cont = st.container()
    
        cont.write ("Nuestro servicio de datos se basan en dos pilares escenciales: El uso de la Inteligencia Artificial y las competencias analiticas y empresariales de nuestro equipo. Nuestra fuerza proviene de una combinación única de tecnologia de datos de ultima generacion, métodos ágiles que permiten entregar proyectos muy rápido y un equipo formado por los mejores expertos en sus campos (consultores de negocios, analistas de datos, científicos de datos, ingenieros de datos y especialistas en hotelería y turismo.")

        

    if box=="Descubre Madrid":  

       st.title("Nuestra ciudad: ") 

       st.subheader("Madrid es la 1ª ciudad de España y la 4ª del mundo mejor preparada para el turismo")

       st.video("https://www.youtube.com/watch?v=-Xv5rw_Xv8c")

       st.markdown("# Por que Madrid:")

       st.image("XqMadrid.JPG")

       st.markdown("# Dividida en 21 distritos y 128 barrios, Madrid ofrece una oferta turistica impresionate y para todo tipo de clientes : ")

       plt.ion()
       plt.figure(figsize=(10,6))
       sns.scatterplot(x=data.longitude,y=data.latitude,hue=data.neighbourhood_group)
       st.pyplot()

       st.markdown("- Vemos en la imagen la distribución de anuncios por distrito")

     
#Hasta aqui.
       

   
    
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




