import pandas as pd
from tkinter import messagebox as mx

def repeticion_valores(data, dias_semana):
    try:
        # Creamos un dataframe 
        columns=["Fecha", "Lider", "PCRC","#Skill", "Plataforma", "ID", "DNI", "Nombre y Apellido","Horario",  "0:00", "0:30", "1:00", "1:30", "2:00", "2:30", "3:00", "3:30", "4:00", "4:30", "5:00", "5:30", "6:00", "6:30", "7:00", "7:30", "8:00", "8:30", "9:00", "9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30","23:00", "23:30"]
        df = pd.DataFrame(columns= columns)
        data[0]
        # Creamos un contador que nos permita indicar el indice donde queremos colocar el dato
        contador = 0

        # Colocamos los datos
        for d in data:
            for x in range(7):
                contador = contador  + 1
                df.loc[contador, "Fecha"] = dias_semana[x]
                df.loc[contador, "Lider"] = d[6]
                df.loc[contador, "PCRC"] = d[5]
                df.loc[contador, "#Skill"] = d[4]
                df.loc[contador, "ID"] = d[3]
                df.loc[contador, "Nombre y Apellido"] = d[2].replace(",", "")
                df.loc[contador, "DNI"] = d[1]
                df.loc[contador, "Horario"] = d[7]

        df["Plataforma"] = "GSS ARG"
        # Cambiamos el formato de los pcrc 
        for i in range(1, len(df)):
            if df.loc[i, "PCRC"] == "1L convergente":
                df.loc[i, "PCRC"] = "1L CONVERGENTE COM"
            elif df.loc[i, "PCRC"] == "1L Convergente":
                df.loc[i, "PCRC"] = "1L CONVERGENTE COM"
            elif df.loc[i, "PCRC"] == "1L convergente cross":
                df.loc[i, "PCRC"] = "1L CONVERGENTE CROSSELLING"

        df["Nombre y Apellido"] = df["Nombre y Apellido"].replace(",", "")
    except Exception as e:
        mx.showerror("Repeticion valores", f"Se produjo un error en la funcion que se encarga de coloca los valores iniciales en el df principal. Error: {e}")
    # Devolvemos el dataframe
    return df