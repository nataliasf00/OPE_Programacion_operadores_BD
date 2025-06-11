#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import tkinter as tk
import json
import numpy as np
import requests
import pyodbc
import warnings
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from PIL import Image, ImageTk
from openpyxl.styles import PatternFill
from openpyxl import Workbook
import xlsxwriter
import mysql.connector



def cargar_archivos():
    # Borra todo el contenido del Text widget
    text_output.delete('1.0', tk.END)

    ruta_carpeta = ruta_input.get() # Obtener la ruta de la carpeta

    if not os.path.exists(ruta_carpeta):
        mensaje_resultado.config(text="La ruta no existe.", fg="red")
        text_output.insert(tk.END, "La ruta no existe.\n")  # Mostrar mensaje en el Text widget
        
        return
    
    informe = informe_input.get()  # Obtener la fecha del Entry
    
    try:
        archivo = str(informe) + ".csv"
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        mensaje = f"Leyendo archivo: {ruta_archivo}\n"
        text_output.insert(tk.END, mensaje)  # Mostrar mensaje en el Text widget
        
        # Leer el archivo Excel (hoja específica y rango)
        try:
            df = pd.read_csv(ruta_archivo, encoding='latin1', sep=';')
            usuario = 'desarrollo'
            contraseña = 'test_24*'
            host = '192.168.90.32'
            puerto = '3306'
            base_de_datos = 'bdsacomco_controloperaciones'
    
            # Crea la cadena de conexión
            cadena_conexion = f'mysql+mysqlconnector://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}'

            try:
                conn = mysql.connector.connect(
                    host=host,
                    user=usuario,
                    password=contraseña,
                    database=base_de_datos
                )
                cursor = conn.cursor()
                cursor.execute("SELECT MAX(Fecha) FROM programacion_operadores")
                ultima_fecha = cursor.fetchone()[0]

                if ultima_fecha:
                    text_output.insert(tk.END, f"Última fecha de programacion guardada en la base de datos: {ultima_fecha}\n")
                    try:
                        # Crea el motor de conexión
                        motor = create_engine(cadena_conexion)
                        
                        df_renombrado = df.rename(columns={'Compañía': 'compania', 'Asignación': 'asignacion', 'Código de conductor': 'codigo_conductor', 'Conductor': 'conductor', 'Amplitud del servicio': 'amplitud_servicio', 'Tiempo de producción': 'tiempo_produccion', 'Distancia de producción (m)': 'distancia_produccion', 'Parte de trabajo': 'parte_trabajo', 'Tipo de tarea': 'tipo_tarea'})
                        df_renombrado['codigo_conductor'] = df_renombrado['codigo_conductor'].astype(str).str.zfill(4)
                        df_renombrado['Fecha'] = pd.to_datetime(df_renombrado['Fecha'], format='%d/%m/%Y')

                        # Columas como string
                        df_renombrado = df_renombrado.astype({
                            'compania': str,
                            'asignacion': str,
                            'conductor': str,
                            'amplitud_servicio': str,
                            'tiempo_produccion': str,
                            'distancia_produccion': str,
                            'parte_trabajo': int,
                            'tipo_tarea': str
                        })

                        df_renombrado = df_renombrado.rename(columns={'Desde': 'desde', 'Hasta': 'hasta', 'Hora inicio  ': 'hora_inicio', 'Hora fin ': 'hora_fin', 'Duración': 'duracion', 'Distancia (m)': 'distancia_m', 'Servicio vehículo': 'serv_vehiculo', 'Tipo de vehículo': 'tipo_vehiculo', 'Línea': 'linea', 'Ruta ': 'ruta'})

                        # Columas como string
                        df_renombrado = df_renombrado.astype({
                            'desde': str,
                            'hasta': str,
                            'hora_inicio': str,
                            'hora_fin': str,
                            'duracion': str,
                            'distancia_m': str,
                            'serv_vehiculo': str,
                            'tipo_vehiculo': str,
                            'linea': str, 
                            'ruta': str
                        })
                        df_renombrado = df_renombrado.rename(columns={'Vehículo': 'vehiculo', 'Viajes': 'viajes', 'Trayecto  ': 'trayecto'})
                        # Columas como string
                        df_renombrado = df_renombrado.astype({
                            'vehiculo': str,
                            'viajes': str,
                            'trayecto': str
                        })
                        
                        
                        df_renombrado.to_sql('programacion_operadores', con=motor, if_exists='append', index=False)
                        
                        text_output.insert(tk.END, f"Cantidad de registros a insertar: {len(df)}\n")
                        mensaje_resultado.config(text="Los datos se han insertado correctamente en la base de datos", fg="green")
                        text_output.insert(tk.END, "Los datos se han insertado correctamente en la base de datos\n")  # Mostrar mensaje de error en el Text widget
                        
                    except Exception as e: 
                        text_output.insert(tk.END, "Ocurrió un error al insertar los datos\n")  # Mostrar mensaje de error en el Text widget
                        text_output.insert(tk.END, f"{e}\n")  # Mostrar mensaje de error en el Text widget
                else:
                    text_output.insert(tk.END, "No se encontraron fechas en la base de datos.\n")
                cursor.close()
                conn.close()
            except Exception as e:
                text_output.insert(tk.END, f"Error al consultar la última fecha: {e}\n")   
        except Exception as e:
            mensaje = f"Error al leer el archivo {archivo}: {e}\n"
            text_output.insert(tk.END, mensaje)  # Mostrar mensaje de error en el Text widget
    except Exception as ex:
        mensaje2 = ex
        text_output.insert(tk.END, mensaje2)  # Mostrar mensaje en el Text widget            
        return  

def consulta_fecha():
    usuario = 'desarrollo'
    contraseña = 'test_24*'
    host = '192.168.90.32'
    puerto = '3306'
    base_de_datos = 'bdsacomco_controloperaciones'

    try:
        conn = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contraseña,
            database=base_de_datos
        )
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(Fecha) FROM programacion_operadores")
        ultima_fecha = cursor.fetchone()[0]
    
        if ultima_fecha:
            text_output.insert(tk.END, f"Última fecha de programacion guardada en la base de datos: {ultima_fecha}\n")
        else:
            text_output.insert(tk.END, "No se encontraron fechas en la base de datos.\n")
        cursor.close()
        conn.close()
    except Exception as e:
        text_output.insert(tk.END, f"Error al consultar la última fecha: {e}\n")   
        return

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programacion operadores")  # Título de la ventana
ventana.geometry("1000x700")  # Tamaño de la ventana
ventana.config(bg="white")  # Fondo blanco

# Cargar la imagen
ruta_imagen = r"Z:\GERENCIA\PUBLICA\logo sao.png"
imagen = Image.open(ruta_imagen)

# Obtener las dimensiones originales de la imagen
ancho_original, alto_original = imagen.size

# Redimensionar la imagen a 250 píxeles de ancho manteniendo la relación de aspecto
nuevo_ancho = 250
nuevo_alto = int((nuevo_ancho / ancho_original) * alto_original)
imagen_redimensionada = imagen.resize((nuevo_ancho, nuevo_alto))

# Convertir la imagen redimensionada en un formato compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Crear un Label para la imagen y colocarla en la esquina superior izquierda
etiqueta_imagen = tk.Label(ventana, image=imagen_tk, bg="white")
etiqueta_imagen.place(x=10, y=10)  # Ubicar la imagen en la esquina superior izquierda

# Crear un Label para el título "PROGRAMACION DE OPERADORESA BD" con color verde oscuro y una fuente más delgada
titulo = tk.Label(ventana, text="PROGRAMACION DE OPERADORES A BASE DE DATOS", font=("Aptos Narrow", 20, "bold"), bg="white", fg="#005639")
# Centrar el título en la ventana, debajo de la imagen
titulo.place(relx=0.5, rely=0.2, anchor="center")

# Crear un Label para el mensaje debajo del título
mensaje = tk.Label(ventana, text="Ingrese la ruta donde están las programaciones", font=("Aptos Narrow", 12), bg="white", fg="black")
# Centrar el mensaje en la ventana, justo debajo del título
mensaje.place(relx=0.5, rely=0.3, anchor="center")

# Crear un cuadro de texto (input) para ingresar la ruta con tamaño específico (por ejemplo, 40 caracteres de ancho)
ruta_input = tk.Entry(ventana, font=("Aptos Narrow", 11), width=80, bd=2, relief="solid", highlightthickness=2, highlightbackground="#746f74", highlightcolor="#746f74")
# Colocar el cuadro de texto debajo del mensaje
ruta_input.place(relx=0.5, rely=0.35, anchor="center")

# Crear un Label para el mensaje debajo del título
mensaje2 = tk.Label(ventana, text="Ingrese el nombre del archivo .csv con la programación de los operadores", font=("Aptos Narrow", 12), bg="white", fg="black")
# Centrar el mensaje en la ventana, justo debajo del título
mensaje2.place(relx=0.5, rely=0.45, anchor="center")

# Crear un cuadro de texto (input) para ingresar la ruta con tamaño específico (por ejemplo, 40 caracteres de ancho)
informe_input = tk.Entry(ventana, font=("Aptos Narrow", 11), width=40, bd=2, relief="solid", highlightthickness=2, highlightbackground="#746f74", highlightcolor="#746f74")
# Colocar el cuadro de texto debajo del mensaje
informe_input.place(relx=0.5, rely=0.5, anchor="center")

# Crear un botón debajo del Entry con texto "Cargar Novedades", fondo verde medio y texto blanco
boton_cargar = tk.Button(ventana, text="CARGAR ARCHIVO", font=("Aptos Narrow", 11, "bold"), bg="#46913C", fg="white", relief="flat", width=21, height=2, command=cargar_archivos)
# Colocar el botón un poco más hacia el centro
boton_cargar.place(relx=0.63, rely=0.6, anchor="center")

# Crear un segundo botón alineado con el primero
boton_consulta_fecha = tk.Button(ventana, text="CONSULTA FECHA", font=("Aptos Narrow", 11, "bold"), bg="#46913C", fg="white", relief="flat", width=21, height=2, command=consulta_fecha)
# Colocar el botón a la derecha del primero, más centrado
boton_consulta_fecha.place(relx=0.37, rely=0.6, anchor="center")


# Crear un Label para mostrar el mensaje debajo del botón
mensaje_resultado = tk.Label(ventana, text="", font=("Aptos Narrow", 8), bg="white", fg="black")
# Centrar el mensaje debajo del botón
mensaje_resultado.place(relx=0.5, rely=0.7, anchor="center")

# Crear un Text widget para mostrar los mensajes de print
text_output = tk.Text(ventana, font=("Aptos Narrow", 10), height=10, width=100, wrap=tk.WORD, bd=2, relief="solid")
# Colocar el Text widget debajo del mensaje_resultado
text_output.place(relx=0.5, rely=0.85, anchor="center")

# Iniciar la interfaz
ventana.mainloop()


# In[ ]:




