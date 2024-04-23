from conectar import *
from bson import json_util
import json

db = con()
coleccion = db.alumnos
documentos = coleccion.find()

resultado = []

for documento in documentos:
    documento ['_id']= str(documento['_id'])
    resultado.append(documento)

print(json_util.dumps(resultado, indent=4))