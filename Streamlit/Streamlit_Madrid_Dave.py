
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np


st.set_page_config(layout="wide")


header = st.container()
dataset = st.container()



with header:
    st.title("WELCOME TO MADRID! :tada: :smile:")

with dataset:
    st.title("Madrid Airbnb :hotel:")    
    madrid_data = pd.read_csv("madrid_airbnb.csv")
    st.write(madrid_data.head(50))

    st.map (
       
    )