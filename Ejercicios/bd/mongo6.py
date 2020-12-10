# metodos de listado de documentos en colecciones
# Operadores en MongoDB --> https://docs.mongodb.com/manual/reference/operator/query/

from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']

print("\nListando")
#Listando
for documento in coleccion.find({}):
    print(documento)

print("\nListando con condicion 1")

#Listando con condicion 1
for documento1 in coleccion.find({
    "poblacion": {
        "$gt": 25000
    }
}):
    print(documento1)

print("\nListando con condicion 2")

#Listando con condicion 2
for documento2 in coleccion.find({
    "depto": {
        "$eq": "San Salvador"
    }
}):
    print(documento2)

print("\nObteniendo solamente un documento")
#Obteniendo solamente un documento
documento3 = coleccion.find_one({
    "municipio": {
        "$eq": "Sonsonate"
    }
    })
print(documento3)