#Debemos importar la libreria, directiva import
import sqlite3

#crear (abrir) una conexión
conexion=sqlite3.connect("PrimeraConexion")

#para poder interactuar con la BD necesitamos de un puntero/cursor
cursor = conexion.cursor()

#Ejecutar query (consulta)
cursor.execute("CREATE TABLE ALUMNOS (nombre_alumno VARCHAR(50), edad_alumno INTEGER, nombre_curso VARCHAR(50))")

#Insertar registros en una tabla
cursor.execute("INSERT INTO ALUMNOS VALUES ('Erick Cruz',30,'Python3')")
#conexion.commit()

#Insertar varios registros en una tabla
#en lugar de varios INSERT

varios_alumnos=[
                ("Laura",20,"Java"),#tuplas
                ("Juan",23,"C#"),
                ("Pedro",22,"Java"),
                ("Ana",30,"Python 3"),
                ("Susana",25,"Python 3")#última tupla sin ,
                ]
#ejecuta muchos, para varios registros
#? el número de campos a utilizar
cursor.executemany("INSERT INTO ALUMNOS VALUES (?,?,?)", varios_alumnos)
#primer parámetro de executemany es el Query y el segundo es la lista
conexion.commit()

#Listar registros
cursor.execute("SELECT * FROM ALUMNOS")
lista_registros=cursor.fetchall()
#fetchall devuelve una lista con todos los registros
print(lista_registros)
conexion.commit()

print("---------------------------")

#Listar registros 2
cursor.execute("SELECT * FROM ALUMNOS")
lista_registros=cursor.fetchall()
for alumno in lista_registros:
    print(alumno)
conexion.commit()

print("---------------------------")

#Listar registros 3
cursor.execute("SELECT * FROM ALUMNOS")
lista_registros=cursor.fetchall()
for alumno in lista_registros:
    print("El alumno ",alumno[0], " inscrito en ",alumno[2])
conexion.commit()

#cerrar la conexión
conexion.close()

#ejecutamos y revisamos la carpeta