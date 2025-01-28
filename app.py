import customtkinter as ctk
import pandas as pd
import openpyxl
from tkinter import filedialog
from datetime import datetime, timedelta
from tkinter import messagebox as mx
from procesamiento_progra.preparacion_df_inicial import repeticion_valores
from procesamiento_progra.colocacion_unos import colocacion_horarios
from procesamiento_progra.preparacion_dnh import filtrado_de_columnas, obtencion_datos
from config import Config

def main(fecha_str, entry_archivo):
    # convertimos ese dato en fecha
    fecha = datetime.strptime(fecha_str.get(),"%d-%m-%Y")

    # Creamos una lista vacia para poder almacenar las fechas que necesitamos
    dias_semana = []

    # Almacenamos las fechas
    dias_semana.append(fecha_str.get())
    for i in range(1, 7):
        dia = fecha + timedelta(days=i)
        dia = dia.strftime("%d-%m-%Y")
        dias_semana.append(dia)
    
    # Hacemos global la variable dias semana
    Config.dias_semana = dias_semana
    print(dias_semana)

    # Creamos un df con el excel importado
    dota = pd.read_excel(Config.ruta_dotacion, usecols=["PROVEEDOR", "DNI", "NOMBRE Y APELLIDO Asesor" ,"LOG ID AVAYA", "SKILL", "PCRC", "LIDER", "HORARIO"])

    # Convertimos los datos a una matriz de numpy
    data = dota.to_numpy()

    # Procesamos los valores en pandas
    df_inicial = repeticion_valores(data, dias_semana)

    # eliminamos los espacios que hay antes o despues de los horarios
    df_inicial['Horario'] = df_inicial['Horario'].str.strip()

    # Convertimos nuevamente a np para un mejor manejo de datos
    matriz = df_inicial.to_numpy()

    # Establecemos una lista con los horarios
    horarios_list = Config.horarios_list    
    # Comenzamos a rellenear los espacios en blanco con datos 
    for m in matriz:
        
        # Solo tomamos los dias que no sean fines de semana 
        if m[0] != dias_semana[0] and m[0] != dias_semana[1]:

            # Ejecutamos la funcion que coloca los unos dependiendo el horario
            colocacion_horarios(m[8], horarios_list, m)
    
    # ---- Preparamos le dnh para la extraccion de datos ---- #
    df_dnh = pd.read_excel(Config.ruta_dnh)

    indices_columnas = filtrado_de_columnas(df_dnh, dias_semana[0])
    df_borrar = obtencion_datos(df_dnh, indices_columnas)

    # Recorremos la progra
    for m in matriz:
        
        # Condicional para que solamente me filtre solamente los dias no habiles
        if m[0] == dias_semana[0]:

            # Recorremos el df_borrar comparando los id 
            for index_borrar in df_borrar.index:
                
                if m[5] == df_borrar.loc[index_borrar, "Id Avaya"]:
                    horario_borrar = df_borrar.loc[index_borrar, "Horarios"]
                    horarios_list = Config.horarios_list

                    colocacion_horarios(horario_borrar, horarios_list, m)
                    
        
    
    # Repetimos le mismo procedimiento pero con dias_semana[1]
    indices_columnas = filtrado_de_columnas(df_dnh, dias_semana[1])
    df_borrar = obtencion_datos(df_dnh, indices_columnas)

    # Recorremos la progra
    for m in matriz:
        
        # Condicional para que solamente me filtre solamente los dias no habiles
        if m[0] == dias_semana[1]:

            # Recorremos el df_borrar comparando los id 
            for index_borrar in df_borrar.index:
                
                if m[5] == df_borrar.loc[index_borrar, "Id Avaya"]:
                    
                    # Creamos variables
                    horario_borrar = df_borrar.loc[index_borrar, "Horarios"]
                    horarios_list = Config.horarios_list
                    colocacion_horarios(horario_borrar, horarios_list, m)


    # Convertimos en dataframe una vez procesados los datos
    columns=["Fecha", "Lider", "PCRC","#Skill", "Plataforma", "ID", "DNI", "Nombre y Apellido","Horario",  "0:00", "0:30", "1:00", "1:30", "2:00", "2:30", "3:00", "3:30", "4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30","23:00", "23:30"]
    df = pd.DataFrame(matriz, columns=Config.columns)

    # Exportamos los datos a excel
    df.to_excel(f"{Config.ruta_salida}{entry_archivo.get()}.xlsx",engine="openpyxl", index=False)
    if df.to_excel:
        mx.showinfo("Exportacion exitosa", f"El documento se exporto exitosamente. {entry_archivo.get()}")


# Creacion de ventana principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
ventana_principal = ctk.CTk()
ventana_principal.geometry("550x600")
ventana_principal.title("Ventana Principal")

# Creamos un frame
frame_title = ctk.CTkFrame(ventana_principal)
frame_title.pack(pady=5, padx=5, fill ="both")

# Creacion de titulo
title_label = ctk.CTkLabel( frame_title, text="Automatizacion Progra", font=("Helvetica", 20, "bold"))
title_label.pack(pady=15, padx=5)

def abrir_archivo_dotacion():
    Config.ruta_dotacion = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Todos los archivos", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if Config.ruta_dotacion:
        label_ruta_dotacion.configure(text=f"Archivo seleccionado:\n{Config.ruta_dotacion}")

def abrir_archivo_dnh():
    Config.ruta_dnh = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[("Todos los archivos", "*.txt"), ("Todos los archivos", "*.*")]
    )
    if Config.ruta_dnh:
        label_ruta_dnh.configure(text=f"Archivo seleccionado:\n{Config.ruta_dnh}")

# Label dotacion
frame_dotacion = ctk.CTkFrame(ventana_principal)
frame_dotacion.pack(pady=5, padx=5, fill = "both")
label_dotacion = ctk.CTkLabel(frame_dotacion, text="Seleccione el archivo de la dotacion", font=("Helvetica", 14))
label_dotacion.pack(pady=5, padx=5)

# Boton para abrir el explorador de archivos
frame_boton = ctk.CTkFrame(frame_dotacion,fg_color="#2d2d2d")
frame_boton.pack(pady=5, padx=2)
explorardor = ctk.CTkButton(frame_boton, text="Seleccionar archivo", command=abrir_archivo_dotacion)
explorardor.pack(pady=1, padx=1)

# Etiqueta para mostrar la ruta del archivo seleccionado
label_ruta_dotacion = ctk.CTkLabel(frame_dotacion, text="Archivo seleccionado: Ninguno")
label_ruta_dotacion.pack(pady=5)

# frame_seleccionar_dnh
frame_dnh = ctk.CTkFrame(ventana_principal)
frame_dnh.pack(pady=5, padx=5, fill = "both")
label_dnh = ctk.CTkLabel(frame_dnh, text="Seleccione el archivo del dnh", font=("Helvetica", 14))
label_dnh.pack(pady=5, padx=5)

# Boton para abrir el explorador de archivos
frame_boton = ctk.CTkFrame(frame_dnh,fg_color="#2d2d2d")
frame_boton.pack(pady=5, padx=2)
explorardor = ctk.CTkButton(frame_boton, text="Seleccionar archivo", command=abrir_archivo_dnh)
explorardor.pack(pady=1, padx=1)

# Etiqueta para mostrar la ruta del archivo seleccionado
label_ruta_dnh = ctk.CTkLabel(frame_dnh, text="Archivo seleccionado: Ninguno")
label_ruta_dnh.pack(pady=5)

# Indicar fecha
frame_fecha = ctk.CTkFrame(ventana_principal)
frame_fecha.pack(pady=5, padx=5, fill = "both")
label_fecha = ctk.CTkLabel(frame_fecha, text="Ingrese la fecha del dia sabado", font=("Helvetica", 14))
label_fecha.pack(pady=5, padx=5)
fecha = ctk.CTkEntry(frame_fecha, placeholder_text="DD/MM/YYYY")
fecha.pack(pady=5, padx=5)

# nombre archivo resultado
frame_archivo = ctk.CTkFrame(ventana_principal)
frame_archivo.pack(pady=5, padx=5, fill = "both")
label_archivo = ctk.CTkLabel(frame_archivo, text="Coloque el nombre del archivo final", font=("Helvetica", 14))
label_archivo.pack(pady=5, padx=5)
entry_archivo = ctk.CTkEntry(frame_archivo, placeholder_text=".xlsx" )
entry_archivo.pack(pady=5, padx=5)


# boton cotinuar
frame_continuar = ctk.CTkFrame(ventana_principal)
frame_continuar.pack(pady=5, padx=5)
continuar = ctk.CTkButton(frame_continuar, text="Finalizar", command=lambda:main(fecha, entry_archivo))
continuar.pack(pady=5, padx=5)

ventana_principal.mainloop()






