#eliminar documentos
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']
coleccion.delete_one({
    "depto":"San Salvador"
})
documento = coleccion.find_one({
    "depto":"San Salvador"
})
print(documento+"\n")

#comprobando
for documento in coleccion.find({}):
    print(documento)