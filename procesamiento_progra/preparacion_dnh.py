import pandas as pd
from datetime import datetime
def filtrado_de_columnas (df, dias_semana):
    # Necesitamos tratar el input dias_semana
    dias_semana = dias_semana.replace("/", "-")

    # Usar .str.contains() para identificar las columnas que cumplen la condición
    mascara = df.columns.str.contains(dias_semana)
    indices_columnas = [i for i, flag in enumerate(mascara) if flag]

    print(f"Índices de las columnas con {dias_semana}:", indices_columnas)
    return indices_columnas


def obtencion_datos (df, indices_columnas):
    # creamos un df para almacenar los datos obtenidos
    df_borrar = pd.DataFrame(columns=["Id Avaya","Horarios"])

    # Creamos un contador para poder indicar en que indice del df colocaremos los datos
    contador = 0

    Contador_index = 0 # Creamos este contador para corroborar la cantidad de asesores que trabajan los dias no habiles

    # Recorremos toda la columna para ver que valores no son nulos y en caso de encontrar un valor no nulo, obtenemos el id del asesor
    for index in df.index:

        # Extraer las columnas de interés para esta fila
        valores = df.iloc[index, indices_columnas]

        # Verificar si hay al menos un valor no nulo
        if valores.notna().any():  # .notna() identifica los valores no nulos
            # id avaya
            avaya = df.loc[index, 'Avaya']
            horario = df.iloc[index, indices_columnas[0]]
            print(f"Fila {index}: ID del asesor = {avaya}")
            Contador_index = Contador_index + 1
            contador = contador + 1

            # Agregamos los datos al df
            df_borrar.loc[contador, "Id Avaya"] = avaya
            df_borrar.loc[contador, "Horarios"] = horario
        
    print(Contador_index)
    return df_borrar

            
