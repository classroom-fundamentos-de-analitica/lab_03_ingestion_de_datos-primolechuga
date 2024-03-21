"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    # Leer el archivo
    txt = open('clusters_report.txt', 'r')
    lines = txt.readlines()
    txt = str(txt.read())

    indices = re.split(r'\s\s+', lines[0])[:-1]
    linea2 = lines[1].split("  ")[5].replace(" ", "_").lower()

    for i in range(len(indices)):
        indices[i] = indices[i].replace(" ", "_").lower()
        if indices[i][-2:] == "de":
            indices[i] = "_".join([indices[i], linea2])[:-1]

    lines = lines[2:]
    cluster,cantidad,porcentaje,claves =[],[],[],[]
    
    pt1 = r'\d+(?:\,\d+)?'
    pt2 = r'[a-zA-Z].*\n'
    indice = 0
    for i in lines :
        numero = re.findall(pt1, i)
        clave = re.findall(pt2, i)
        if numero:
            cantidad.append(int(numero[1]))
            porcentaje.append(float(numero[2].replace(',', '.')))
            cluster.append(int(numero[0]))
            claves.append(clave[0].replace('\n',''))
        elif len(clave) > 0:
           claves[-1] = re.sub(r'\s+', ' ', claves[-1] + clave[0].replace('\n','').replace('.',''))
    
    df = pd.DataFrame({indices[0]: cluster, indices[1]: cantidad, indices[2]: porcentaje, indices[3]: claves})
    df = df.set_index(indices[0])

    return df