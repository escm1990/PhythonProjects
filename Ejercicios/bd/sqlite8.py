import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos3")
cursor = conexion.cursor()

#UPDATE CON WHERE
#cursor.execute("UPDATE CURSOS SET cupos_curso=87 WHERE nombre_curso = 'Java'")

#DELETE CON WHERE
cursor.execute("DELETE FROM CURSOS WHERE nombre_curso = 'Java'")

#SELECT CON WHERE
cursor.execute("SELECT * FROM CURSOS WHERE nombre_curso = 'Java'") #case sensitive

loscursos=cursor.fetchall()
print(loscursos)
conexion.commit()

conexion.close()