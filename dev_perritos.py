# -*- coding: utf-8 -*-
"""
@author: yosel
"""

import streamlit as st
st.title("Compra de Arneses y Botas para perros")
st.header("Tienda RED")
st.subheader("Ingrese los datos de su perro")
def confirmar(entrada,prediccion):
    if(entrada>prediccion):
        mensaje="Las botas que has seleccionado podrían ser DEMASIADO GRANDES para un perro tan pequeño como el suyo. Recomendamos unas botas de tamaño",str(round(prediccion))
        print(entrada)
        st.error(mensaje)
    elif(entrada<prediccion):
        mensaje="Las botas que has seleccionado podrían ser DEMASIADO PEQUEÑAS para un perro tan pequeño como el suyo. Recomendamos unas botas de tamaño",str(round(prediccion))
        print(entrada)
        st.error(mensaje)
    else:
        print(entrada)
        mensaje="¡Gran elección! Creemos que estas botas se adaptarán bien a su perro."
        st.success(mensaje)
arnes=0
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        val1 = col1.slider('Tamaño del arnes', 0, 100, 0)
    with col2:
        val2= col2.text_input(label="Tamaño del arnes", value=0)


import joblib
import numpy as np
load_model=joblib.load("perros.pkl")
arnes=int(val1)
inputs=np.array(val1).reshape(-1,1)
predicted_boot_size=load_model.predict(inputs)[0]

if st.button("check"):
    confirmar(int(val2), round(predicted_boot_size))
