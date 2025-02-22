import pandas as pd
import openpyxl 
from config import Config
from datetime import datetime, timedelta
from procesamiento_progra.preparacion_dnh import filtrado_de_columnas, obtencion_datos
from tkinter import messagebox as mx

def procesamiento_dotacion (fecha_input, dotacion, dimensionamiento):
        
    try:   
        # fecha_input = input("Ingrese la fecha del proximo sabado\n")
        df_dimensionamiento = pd.read_excel(dimensionamiento)
        df_dotacion = pd.read_excel(dotacion, usecols=["PROVEEDOR", "DNI", "NOMBRE Y APELLIDO Asesor" ,"LOG ID AVAYA", "SKILL", "PCRC", "LIDER", "HORARIO"])


        ######## Colocacion de fecha para el filtrado de las columnas ##########
        # convertimos ese dato en fecha
        fecha = datetime.strptime(fecha_input,"%d-%m-%Y")

        # Creamos una lista vacia para poder almacenar las fechas que necesitamos
        dias_semana = []

        # Almacenamos las fechas
        dias_semana.append(fecha_input)
        for i in range(1, 7):
            dia = fecha + timedelta(days=i)
            dia = dia.strftime("%d-%m-%Y")
            dias_semana.append(dia)
    except Exception as e:
        mx.showerror("Error al convertir fecha", f"{e}")

    try:
        # Dia sabado
        columnas_filtradas = filtrado_de_columnas(df_dimensionamiento, dias_semana[0])
        df_borrar = obtencion_datos(df_dimensionamiento, columnas_filtradas)

        # Variable que nos cuenta la cantidad de asesores que tienen en su horario del DNH "vacaciones"
        contador = 0

        # Recorremos el dataframe df_borrar buscando los asesores que tengan en su horario "vacaciones"
        for x in df_borrar.index:
            if df_borrar.loc[x, "Horarios"] == "vacaciones":
                avaya_borrar = df_borrar.loc[x, "Id Avaya"]
                contador += 1
                # filtrar la dotacion y que siempre que el id sea uno de estos. que modifique la columna horarios con "vacaciones"
                for d in df_dotacion.index:
                    if df_dotacion.loc[d, "LOG ID AVAYA"] == avaya_borrar:
                        df_dotacion.loc[d, "HORARIO"] = "vacaciones"
    except Exception as e:
        mx.showerror("Procesamiento Sabado", f"Se produjo un error al intentar procesar la dotacion:\n {e}")
    try:
        # Dia Domingo
        columnas_filtradas = filtrado_de_columnas(df_dimensionamiento, dias_semana[1])
        df_borrar = obtencion_datos(df_dimensionamiento, columnas_filtradas)

        # Recorremos el dataframe df_borrar buscando los asesores que tengan en su horario "vacaciones"
        for x in df_borrar.index:

            if df_borrar.loc[x, "Horarios"] == "vacaciones" or df_borrar.loc[x, "Horarios"] == " vacaciones" or df_borrar.loc[x, "Horarios"] == "vacaciones " :
                avaya_borrar = df_borrar.loc[x, "Id Avaya"]
                contador += 1
                # filtrar la dotacion y que siempre que el id sea uno de estos. que modifique la columna horarios con "vacaciones"
                for d in df_dotacion.index:
                    if df_dotacion.loc[d, "LOG ID AVAYA"] == avaya_borrar:
                        df_dotacion.loc[d, "HORARIO"] = "vacaciones"
                else:
                    print(f"Avaya DNH {avaya_borrar} - Avaya dotacion {df_dotacion.loc[d, "LOG ID AVAYA"]}")
    except Exception as e:
        mx.showerror("Procesamiento Domingo", f"Se produjo un error al intentar procesar la dotacion:\n {e} ")

    print("Cantidad de asesores de vacaciones: ",contador)
    ## Hay que arreglar los PCRC
    for index in df_dotacion.index:
        if df_dotacion.loc[index, "SKILL"] == 862:
            df_dotacion.loc[index, "PCRC"] = "CONTROL DE CARGA FIJA"
            df_dotacion.loc[index, "LIDER"] = Config.lider_BO
        elif df_dotacion.loc[index, "SKILL"] == 1160:
            df_dotacion.loc[index, "PCRC"] = "CLOOPERS"
            df_dotacion.loc[index, "LIDER"] = Config.coordinador_operacion
    return df_dotacion




