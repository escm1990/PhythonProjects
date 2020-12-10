#modificando documentos
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']
coleccion.update_one({
    "depto":"Sonsonate"
}, {
    "$set": {
    "depto":"Morazán"   
    }
})

for documento in coleccion.find({}):
    print(documento)