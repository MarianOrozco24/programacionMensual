import pandas as pd
import openpyxl 
from config import Config
from datetime import datetime, timedelta
from procesamiento_progra.preparacion_dnh import filtrado_de_columnas, obtencion_datos

def procesamiento_dotacion (fecha_input, dotacion, dimensionamiento):
        
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

    # Dia sabado
    columnas_filtradas = filtrado_de_columnas(df_dimensionamiento, dias_semana[0])
    df_borrar = obtencion_datos(df_dimensionamiento, columnas_filtradas)
    df_borrar.to_excel("probadno.xlsx", index=False)

    df_borrar.to_excel("borrar.xlsx")
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


    # Dia Domingo
    columnas_filtradas = filtrado_de_columnas(df_dimensionamiento, dias_semana[1])
    df_borrar = obtencion_datos(df_dimensionamiento, columnas_filtradas)
    df_borrar.to_excel("probadno.xlsx", index=False)

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


    print("Cantidad de asesores de vacaciones: ",contador)

    return df_dotacion

    # Dia Domingo


