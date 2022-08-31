import streamlit as st
import pandas as pd
import pydeck as pdk   
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from streamlit_option_menu import option_menu


#Se quita aviso de pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)

#Se importa csv
data = pd.read_csv("madrid_airbnb.csv")

#Se limpian los datos
dfName = data["name"].mode()[0]
data["name"].fillna(dfName, inplace=True)

dfhost_name = data["host_name"].mode()[0]
data["host_name"].fillna(dfhost_name, inplace=True)

data["last_review"].fillna("No Reviews", inplace=True)

data["reviews_per_month"].fillna(0, inplace=True)

#SideBar
with st.sidebar:
#NavBar
    selected = option_menu( "Home Madrid", ["Home", "Datos", "Outliers", "Contacto"],
        icons=["house", "geo-alt", "graph-up","chevron-bar-expand", "chat"],  # optional
        menu_icon="cast",  # optional
        default_index=0)

   # st.metric(label="Prices", value="70$ ", delta="1.2 $")

#Creamos aprtado para Home

if selected == "Home":

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

        
        

if selected== "Datos":

    st.header("Base de datos Madrid Airbnb:")

#Vizualizacion de la Base de Datos
    st.markdown("Se puede mostrar parte de la base datos para su visualizacion: ")
    st.write(data.head(20))
    
#Visualizacion de los distritos degun su precio
    st.subheader("Distritos segun su precio:")
    plt.scatter(data["price"],data["neighbourhood_group"])
    plt.title("Scatter Plot")
    st.pyplot()

#Visualizacion de los distritos degun su cantidad de anuncios

    st.subheader("Distritos segun su cantidad de anuncios:")
    st.bar_chart((data['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count" )

    # Podemos observar mejor los datos con plotly
    fig = px.bar((data['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count", color= (data['neighbourhood_group'].value_counts()),title="Distritos de Madrid")
    st.plotly_chart(fig)


#Visualizacion de los barrios del centro
    st.subheader("Distrito del Centro por precio:")
    st.markdown("""
    - Como hemos podido apreciar según los graficos anteriores, en el distrito del centro tenemos mayor cantidad de anuncios; asi que, vamos a explorar en  que barrios se concentran más dichos anuncios """)
    datos_centro = data[data["neighbourhood_group"].str.contains("Centro")]
    fig = px.bar((datos_centro['neighbourhood'].value_counts()).to_frame(name="count"), y="count", color=datos_centro['neighbourhood'].value_counts(),title = 'Barrios del Centro')
    st.plotly_chart(fig)

#Visualizacion de los hospedajes segun su precio
    st.subheader("Tipo de hospedaje segun su precio:")
    plt.scatter(data["room_type"],data["price"])
    plt.title("Scatter Plot")
    st.pyplot()
    
    st.markdown("Lo observamos con otro grafico")
    values = data.room_type.value_counts()
    names = data.room_type.unique().tolist()
    fig = px.pie(data, values=values, names=names)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig)

#Creamos apartado de Outliers

if selected== "Outliers":
    
    st.header ("Valores atipicos o anomalos")
    st.markdown("Hemos comprobado que la existencia de eventos en determinadas fechas y localización aumenta los precios de los inmuebles en alquiler.")
    
    option = st.selectbox(
            'Outliers más significativos',
            ('Final Champions 2019', 'Pandemia 2020'))

    if option == "Final Champions 2019":
    
        st.header("Caso 1: Final de la Champions 2019  :soccer:") 

        st.markdown("""Despues de analizar los datos nos dimos cuenta de una cantidad significativa de anuncios mostraban estar en alquiler cerca a la fecha de la final de la Champions. Por lo que aumentaba el precio medio de los barrios aledaños añ estadio Wanda Metropolitano.  Aunque, tambien observamos anuncios en otros barrios de Madrid para la misma finalidad que significaban mucha diferencia en compración. """)

        st.image("champions.jpg")


        st.subheader("Visualizacion de los datos con relacion a la Champions")
        datos_sanblas = data[data["neighbourhood_group"].str.contains("San Blas - Canillejas")]
        datos_champions = datos_sanblas[datos_sanblas["name"].str.contains("hampion")]
        
        st.write(datos_champions)

    else: 
        st.subheader('Caso 2: Pandemia 2020 :syringe:')

        st.markdown("""  """)

        st.image("madrid_vacio.jpg")


        st.write("Visualizacion de los datos con relacion a la Pandemia : ")
        
        pandemia_abril = data[data["last_review"].str.contains("2020-04")]
        st.write(pandemia_abril.head(20))

        st.markdown("Nos muestra la cantidad de entradas con reviews en abril del año 2020 :")
        pandemia_abril.shape
        st.markdown("""
                        - Se encuentran 73 anuncios en este mes; ya que, fue en abril donde intentificamos los outliers debido a la normativa de Airbnb respecto a los reviews. 
                        - Se observa una menor cantidad de anuncios con reviews debido al confinamiento restrictivo.  
                    """)

        pandemia_mayo = data[data["last_review"].str.contains("2020-05")]
        st.write(pandemia_mayo.head(20))

        st.markdown("Nos muestra la cantidad de entradas con reviews en mayo del año 2020 :")
        pandemia_mayo.shape
        st.markdown(""" 
                        - Se encuentran 60 anuncios en este mes; ya que, fue en mayo el ultimo mes de confinamiento restrictivo.
                        - Fue a partir de junio que el confinamiento paso a ser perimetral; por lo que, se pudo hacer turismo  dentro de la comunidad. 
                    """)


        