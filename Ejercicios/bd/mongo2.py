#Crear una BD con PY
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
print(conexion.list_database_names())
#no aparecela nueva BD porque está vacía