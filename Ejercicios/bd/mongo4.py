#Agregar documento a la colección
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']
coleccion.insert_one({
'depto':'San Salvador',
'municipio':'San Salvador',
'poblacion':200000
})
#comprobando
print(conexion.list_database_names())
print(nueva_bd.list_collection_names())
print(coleccion.count_documents({}))