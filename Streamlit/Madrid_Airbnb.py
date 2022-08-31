
from asyncore import write
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

#Estableciendo la vista de la página como ancha
st.set_page_config(layout="wide")


#Variables
data = pd.read_csv("madrid_airbnb.csv",)
coordinates = data[["latitude", "longitude", "price"]]
price = data["price"]

#Se limpian los datos
dfName = data["name"].mode()[0]
data["name"].fillna(dfName, inplace=True)

dfhost_name = data["host_name"].mode()[0]
data["host_name"].fillna(dfhost_name, inplace=True)

data["last_review"].fillna("No Reviews", inplace=True)

data["reviews_per_month"].fillna(0, inplace=True)

#Se ignora advertencia de error de librerías

st.set_option('deprecation.showPyplotGlobalUse', False)

# Funcion para reducir el margen top
def margin(): 
    st.markdown("""
            <style>
                .css-18e3th9 {
                        padding-top: 1rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)

header = st.container()

        
#MENU 
EXAMPLE_NO = 1


def streamlit_menu(example=1):
    
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            
            selected = option_menu(
                menu_title="Menu",  # required
                options=["Home", "Datos", "Mapas", "Outliers", "Conclusiones"],  # required
                icons=["house", "bar-chart", "map", "exclamation-octagon","eye"],  # optional
                #menu_icon= "cast",  # optional
                default_index=0,  # optional
                styles={
                    "menu-icon":"Data",
                    
                    "menu_title":{"font-family": "Sans-serif"},
                    "nav-link": {"font-family": "Sans-serif", "text-align": "left", "margin":"0px",},
                    #"nav-link-selected": {""}, 
                    })
        return selected



selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Home":
    

    box= st.sidebar.selectbox(" ",["Conoce Data Home","Descubre Madrid"],index=0)

    if box== "Conoce Data Home":

        st.image("Data Home.png")
        
        st.write("")
        
        
        
        
        st.write("Somos una empresa de consultoría de nueva generación especializada en hostelería y turismo, basada en análisis de datos e Inteligencia Artifical")
        
        st.write("")
        st.write("")
        st.write("")
        
        
        
        
        st.subheader("**Transformamos los datos en valor y utilidad para tu negocio**")

        st.image("FotoMadrid.jpg" )
        
        cont = st.container()
    
        cont.write ("Nuestro servicio de datos se basan en dos pilares escenciales: El uso de la Inteligencia Artificial y las competencias analiticas y empresariales de nuestro equipo. Nuestra fuerza proviene de una combinación única de tecnologia de datos de ultima generacion, métodos ágiles que permiten entregar proyectos muy rápido y un equipo formado por los mejores expertos en sus campos (consultores de negocios, analistas de datos, científicos de datos, ingenieros de datos y especialistas en hotelería y turismo.")

        

    if box=="Descubre Madrid":  

       st.title("Nuestra ciudad: ") 

       st.subheader("Madrid es la 1ª ciudad de España y la 4ª del mundo mejor preparada para el turismo")

       st.video("https://www.youtube.com/watch?v=-Xv5rw_Xv8c")

       st.markdown("# Por que Madrid:")

       st.image("XqMadrid.jfif")

       st.markdown("# Dividida en 21 distritos y 128 barrios, Madrid ofrece una oferta turistica impresionate y para todo tipo de clientes : ")

       plt.ion()
       plt.figure(figsize=(10,6))
       sns.scatterplot(x=data.longitude,y=data.latitude,hue=data.neighbourhood_group)
       st.pyplot()

       st.markdown("- Vemos en la imagen la distribución de anuncios por distrito")
    
   
if selected== "Datos":
    margin() 
    

#Vizualizacion de la Base de Datos
    #st.header("Datos")
    with st.sidebar:
        box = st.selectbox(
        'Seleccione una opción',
        ('Dataframe', 'Precios', 'Cantidad de anuncios', "Barrios del Centro", "Hospedajes"))
    if box== "Dataframe":
        st.header("Base de datos Madrid Airbnb:")
        st.markdown("Se puede mostrar parte de la base datos para su visualizacion: ")
        st.dataframe(data.head(20))

    if box== "Precios":
        #Visualizacion de los distritos degun su precio
            
            st.header("Precios por distrito:")
            st.markdown("""Aquí podemos observar algunos outliers de precio en zonas que no son tan céntricas, la explicacion que le podemos dar es que se celebrara algún evento en fechas determinadas.
            """)
            plt.scatter(data["price"],data["neighbourhood_group"])
            plt.title("Scatter Plot")
            st.pyplot()
            


    if box== "Cantidad de anuncios":
        #Visualizacion de los distritos degun su cantidad de anuncios

        st.header("Cantidad de anuncios por distrito:")
        st.bar_chart((data['neighbourhood_group'].value_counts()).to_frame(name="count"), )

        st.markdown("""Comprobamos la hipótesis que en el centro hay una mayor cantidad de hospedajes en alquiler con un 64.5% del total de anuncios.""")

        # Podemos observar mejor los datos con plotly
        fig = px.bar((data['neighbourhood_group'].value_counts()).to_frame(name="count"), y="count", color= (data['neighbourhood_group'].value_counts()),title="Distritos de Madrid")
        st.plotly_chart(fig)
        


    
    if box== "Barrios del Centro":
        #Visualizacion de los barrios del centro
        st.subheader("Barrios del Centro:")
        st.markdown("""
        - Como hemos podido apreciar según los graficos anteriores, en el distrito del centro tenemos mayor cantidad de anuncios; asi que, vamos a explorar en  que barrios se concentran más dichos anuncios """)
        datos_centro = data[data["neighbourhood_group"].str.contains("Centro")]
        fig = px.bar((datos_centro['neighbourhood'].value_counts()).to_frame(name="count"), y="count", color=datos_centro['neighbourhood'].value_counts(),title = 'Barrios del Centro')
        st.plotly_chart(fig)


    if box== "Hospedajes":
        #Visualizacion de los hospedajes segun su precio
        st.header("Tipo de hospedaje:")
        plt.scatter(data["room_type"],data["price"])
        st.markdown("Observamos la relación del precio con el tipo de hospedaje")
        plt.title("Scatter Plot")
        st.pyplot()
        
        st.markdown("Lo observamos con otro gráfico")
        values = data.room_type.value_counts()
        names = data.room_type.unique().tolist()
        fig = px.pie(data, values=values, names=names)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig)




        

if selected == "Mapas":
    margin()

    # Remove whitespace from the top of the page and sidebar
    st.markdown("""
            <style>
                .css-18e3th9 {
                        padding-top: 0rem;
                        padding-bottom: 10rem;
                        padding-left: 5rem;
                        padding-right: 5rem;
                    }
                .css-1d391kg {
                        padding-top: 3.5rem;
                        padding-right: 1rem;
                        padding-bottom: 3.5rem;
                        padding-left: 1rem;
                    }
            </style>
            """, unsafe_allow_html=True)
    header = st.container()
    with header:
        col1, col2, col3 = st.columns(3)
        col1.title("Mapas")
    
    col1, col2, col3 = st.columns(3)
    
    with st.sidebar:
        add_selectbox = st.selectbox(
        "Tipo de mapa",
        ("Densidad", "Precios",))
        #col3.metric(label="Mean Price", value="150$ ", delta="1.2 $")
    
    if add_selectbox == "Densidad":
        st.markdown("Observamos un mapa de calor de la densidad de anuncios")
        

    
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
                extruded=True,)
                ]))

    if add_selectbox == "Precios":
        margin()

        st.markdown("Observamos un mapa de columnas de cada anuncio. La altura de las columnas representa el precio por noche de cada anuncio")
        
        # Map 2


        tooltip = {"html": "Cost <strong>{price}$</strong>",}

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
            


            getFillColor=[150, 3, 0, 255]),],))





if selected == "Outliers":
    margin()
    st.header ("Valores atipicos o anomalos")
    st.markdown("Hemos comprobado que la existencia de eventos en determinadas fechas y localización aumenta los precios de los inmuebles en alquiler.")
    
    with st.sidebar: 
        option = st.selectbox(
            'Outliers más significativos',
            ('Final Champions 2019', 'Pandemia 2020'))

    if option == "Final Champions 2019":
    
        st.header("Caso 1: Final de la Champions 2019  :soccer:") 

        st.markdown("""Despues de analizar los datos nos dimos cuenta de una cantidad significativa de anuncios mostraban estar en alquiler cerca a la fecha de la final de la Champions. Por lo que aumentaba el precio medio de los barrios aledaños añ estadio Wanda Metropolitano.  Aunque, tambien observamos anuncios en otros barrios de Madrid para la misma finalidad que significaban mucha diferencia en compración. """)

        st.image("champion.jpeg")


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

if selected == "Conclusiones":
    margin()
    st.header("Conclusiones")
    st.markdown(""" 

        -  Confirmamos la hipótesis que los barrios céntricos son los más anunciados por la aplicación de Airbnb. Podemos decir, que hay mas oferta; ya que, en el distrito del Centro tenemos un 64% de anuncios. Además, dentro de este distrito tenemos a los tres barrios con más hospedajes los cuales son Embajadores, Universidad y Palacio.

        -  Estamos asumiendo que la oferta va ligada a la demanda en el Centro, pero no podemos corroborar esta hipótesis debido a que nos falta información.


        +  Debido al análisis de precios que hemos realizado, podemos decir que hay una gran variedad para todos los presupuestos del turista. 
    
        +  Deducimos que el propietario prefiere alquilar un apartameto o casa completa antes que una habitación de hotel debido a la alta oferta que se ofrece.
    
        +  También, hemos comprobado que la existencia de eventos en determinadas fechas y  localización aumenta los precios de los inmuebles en alquiler. 
    
        -  Como por ejemplo, tenemos la final de la Champions celebarada en Madrid en el estadio Wanda Metropolitano ubicado en el distrito de San Blas - Canillejas el año 2019. Ya que, el promedio de precio de este distrito aumentó significativamente debido a este evento.
        """)

    st.subheader("Observaciones")
    st.markdown(""" 

        + En algunos casos pudimos observar que algunos propietarios prefieren no poner su nombre y utilizan apodos o distintas combinaciones alfa-numéricas para proteger su privacidad.

   + Vemos que hay propiertarios que tienen más de 100 alojamientos, siendo un ejemplo un host con 163 inmuebles aunciados. 

   + Hemos observado alquileres en el año 2020 durante los meses de confinamiento; ya que, Airbnb solo te permite valorar la experiencia del hospedaje máximo quince dias después del check-out. Entendemos que estos datos son posibles outliers.""")
