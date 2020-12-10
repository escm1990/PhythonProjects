#agregando varias colecciones a la vez
from pymongo import MongoClient
conexion = MongoClient('localhost')
nueva_bd = conexion['bdpy']
coleccion = nueva_bd['salones']
coleccion.insert_many([
{
'depto':'Santa Ana',
'municipio': 'Santa Ana',
'poblacion':125000
},
{
'depto':'Sonsonate',
'municipio': 'Sonsonate',
'poblacion':112000
},
{
'depto':'Chalatenango',
'municipio': 'Chalatenango',
'poblacion':25000
}
])

#comprobando
print(conexion.list_database_names())
print(nueva_bd.list_collection_names())
print(coleccion.count_documents({}))