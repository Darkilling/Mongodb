from conectar import *
from bson import json_util
import json

codigo = input("ingrese el codigo del restaurante: ")

db = con()
coleccion = db.restaurants
documentos = coleccion.find({"restaurant_id": codigo})

resultado = []

for documento in documentos:
    documento ['_id']= str(documento['_id'])
    resultado.append(documento)

print(json_util.dumps(resultado, indent=4))