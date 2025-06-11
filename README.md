# 📌 Programación de operadores a base de datos

[![Estado del Proyecto](https://img.shields.io/badge/status-terminado-ogreen.svg)]()
[![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)]()

## 🚀 Descripción  

**Programación de operadores a base de datos** es una herramienta en Python diseñada para realizar la carga de la programación de operadores a la base de datos de desarrollos.

### 🎯 Propósito  
Cargar la programación de operadores a la base de datos de desarrollos permitiendo tener la información actualizada para demás desarrollos y consultas

### 👥 Público objetivo  
Está dirigido al **Auxiliar de programación de operadores** de la empresa **Sistema Alimentador Oriental**, facilitando la carga de información de la programación de operadores

## 📌 Funcionalidades  

- ✅ **Consulta ultima fecha** de la programación de operadores cargados en la base de datos.  
- ✅ **Ingreso de ruta de carpeta** debido a que las programaciones de operadores se almacenan en carpetas diferentes por periodo de tiempo.
- ✅ **Ingreso nombre de archivo** debido a que se almacena la información por días.

## 🔄 Entradas y Salidas  

### 📥 **Entradas**  
El sistema recibe un archivo de CSV con el contenido detallado de la programación de los operadores

### 📤 **Salidas**  
El sistema genera dos mensajes principales:  
1. **Ultima fecha cargada en la base de datos**
2. **Cantidad de datos ingresados**
3. **Mensaje de carga correcta con cantidad de registros ingresados**

## 📌 Requisitos  

Para ejecutar el proyecto, asegúrate de tener **Python 3.8 o superior** instalado y las siguientes librerías:  

### 📦 **Librerías necesarias**  

| 📦 Librería                | 🔍 Descripción |
|---------------------------|----------------|
| `os`                      | Manejo de archivos y directorios. *(Incluida en Python, no requiere instalación)* |
| `pandas` (`pd`)           | Manipulación y análisis de datos, especialmente para trabajar con **Excel**, **CSV**, etc. |
| `tkinter` (`tk`)          | Creación de interfaces gráficas. *(Incluida en Python, no requiere instalación)* |
| `json`                    | Manejo de datos en formato **JSON**. *(Incluida en Python, no requiere instalación)* |
| `numpy` (`np`)            | Cálculo numérico y trabajo con arreglos multidimensionales. |
| `requests`                | Realizar peticiones HTTP de forma sencilla. Ideal para APIs. |
| `pyodbc`                  | Conexión con bases de datos mediante **ODBC** (SQL Server, Access, etc.). |
| `warnings`                | Manejo de advertencias durante la ejecución del código. *(Incluida en Python, no requiere instalación)* |
| `datetime`, `timedelta`   | Manejo de fechas y tiempos en Python. *(Incluida en Python, no requiere instalación)* |
| `sqlalchemy`              | Toolkit para trabajar con bases de datos SQL de forma **ORM o SQL pura**. |
| `PIL.Image`, `ImageTk`    | Manejo y visualización de imágenes (vía **Pillow**, extensión de `tkinter`). |
| `openpyxl.styles.PatternFill` | Estilizado de celdas en archivos Excel (`.xlsx`) con colores, etc. |
| `openpyxl.Workbook`       | Creación y manipulación de archivos Excel (`.xlsx`). |
| `xlsxwriter`              | Generación avanzada de archivos Excel (`.xlsx`) con formato, gráficos, etc. |
| `mysql.connector`         | Conexión directa a bases de datos **MySQL** desde Python. |


### 🔧 **Instalación de librerías externas**  
Las siguientes librerías deben instalarse manualmente:  

```bash
pip install pandas pillow pyodbc
```

# 📖 Manual de Uso - Interfaz gráfica
![alt text](<interfaz programacion operadores BD.png>)


## 1️⃣ Instrucciones de Uso

1. Presionar doble click en **Cargar programacion operadores a BD.py**
2. Presionar el botón de **CONSULTA FECHA**
3. Revisar la última fecha de programaciones cargada en la base de datos
4. Ingresar la ruta donde están los archivos de las programaciones de los operadores
5. Ingresar el nombre del archivo csv con las programaciones de los operadores
6. Presionar el botón de **CARGAR ARCHIVO**
7. Revisar que en el cuadro de mensajes se lea el archivo, se muestre la ultima fecha de registros en la base de datos
8. Revisar que en el cuadro de mensajes se muestre la cantidad de registros guardados y que la carga se realizo correctamente


## 2️⃣ Aspectos a tener en cuenta

### ❓ ❓ ❓ ❓ ❓ 
Se debe mantener el formato de las programaciones de operadores con los nombres de las columnas y descargarse de manera detallada
**Ejemplo:** Detallado programacion SEMANA 22 VIERNES - LUNES.csv

## 3️⃣ Contacto y Soporte

Para dudas o soporte técnico, contactar a la profesional de Mejoramiento Continuo de Sistema Alimentador Oriental.
