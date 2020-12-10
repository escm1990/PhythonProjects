#Conexión a MongoDB
from pymongo import MongoClient
#solo cuando utilizamos autenticación
'''MongoClient('localhost',
port=27017,
username='user',
password='pass'
)'''
#en este caso que utilizamos un servidor local
conexion = MongoClient('localhost')
print(conexion.list_database_names())
#obtenemos los nombres de las BD en MongoDB