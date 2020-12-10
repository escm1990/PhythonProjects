#Crear una colección en la BD
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']
print(nueva_bd.list_collection_names())
#no aparecen las colecciones porque están vacías