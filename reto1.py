import requests
import json
import csv
url = "https://storage.googleapis.com/resources-prod-shelftia/scrapers-prueba/product.json"

def get_ca(data):
    if type(data)==dict:
        try:
            if data["name"] == "custom_attributes":
                return data
        except Exception as e:
            pass
        for elemento in data:
            resultado=get_ca(data[elemento])
            if resultado:
                return resultado
    elif type(data)==list:
        for elemento in data:
            resultado=get_ca(elemento)
            if resultado:
                return resultado
    return None

def get_propiedades():
    data = requests.get(url).json()
    ca=get_ca(data)#aca ya tenemos el subdict correcto
    valores=ca['value']
    #print(json.dumps(ca, indent=4))
    filas=[]
    columnas=['allergens','sku','vegan','kosher','organic','vegetarian','gluten_free','lactose_free','package_quantity','unit_size','net_weight']
    filas.append(columnas)
    fila=[]
    for valor in valores:
        dic_fila=json.loads(valores[valor])
        #print(json.dumps(dic_fila, indent=4))
        if valor=='es-CR':
            fila.append([dic_fila['allergens']['value'][0]['name']])
            continue
        for columna in columnas[1:]:
            if type(dic_fila[columna]['value']) != list and type(dic_fila[columna]['value'])!= dict:
                dato=dic_fila[columna]['value']
            elif type(dic_fila[columna]['value']) == list:
                dato=dic_fila[columna]['value'][0]['name']
            else:#por si es dict
                dato=dic_fila[columna]['value']['name']
            if columna in ['unit_size','net_weight']:
                dato=float(dato)
            fila.append(dato)
        filas.append(fila)
    with open('salida.csv', 'w',encoding='utf-8') as outfile:
        csvfile = csv.writer(outfile, delimiter=',', lineterminator='\n')
        for fila in filas:
            csvfile.writerow(fila)

get_propiedades()