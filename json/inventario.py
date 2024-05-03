import os
import json
# import math
import re

# Función para extraer el volumen de la descripción
def extraer_info(descripcion):
    # Utiliza una expresión regular para buscar un patrón de volumen en la descripción
    patron_volumen = r"(\bEDT\b|\bEDP\b|\bPARFUM\b|\bELIXIR\b)"
    match = re.search(patron_volumen, descripcion, flags=re.IGNORECASE)
    if match:
        return match.group(1)  # Devuelve el primer grupo de la coincidencia
    else:
        return "null"  # Si no se encuentra el patrón, devuelve "null"


# Obtiene el directorio actual
directorio_actual = os.path.dirname(os.path.realpath(__file__))
os.chdir(directorio_actual)

# Carga el archivo JSON en una variable
with open('inventario.json','r', encoding='utf-8') as f:
    data = json.load(f)

i=0
# Recorre cada objeto en el archivo JSON
for objeto in data:
    # Verifica si el atributo "ciudad" existe en el objeto
    array = [
        objeto["GroupBrand"],
        objeto["ProductLine"],
        objeto["Description"],
        objeto["Type"],
        objeto["Volumen"],
        objeto["Price"]
    ]

    del objeto["GroupBrand"] 
    del objeto["ProductLine"]
    del objeto["Description"]
    del objeto["Type"]
    del objeto["Volumen"]
    del objeto["Price"]

    objeto["id"] = i

    objeto["GroupBrand"] = array[0]
    objeto["ProductLine"] = array[1]
    objeto["Description"] = array[2]
    objeto["Type"] = array[3]
    objeto["Volumen"] = array[4]
    objeto["Price"] = array[5]

        # objeto["Type"] = switch.get(Type)
    i += 1


# Guarda los cambios en el archivo JSON (opcional)
with open('inventario.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
