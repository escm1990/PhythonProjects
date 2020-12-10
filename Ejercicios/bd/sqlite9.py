import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos3")
cursor = conexion.cursor()

elcodigo = int(input("Digite el código del curso que desea consultar: ")),
cursor.execute("SELECT * FROM CURSOS WHERE id_curso = ?",elcodigo)

loscursos=cursor.fetchall()
print(loscursos)

conexion.commit()
conexion.close()