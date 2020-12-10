import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos3")
cursor = conexion.cursor()
loscursos=[
    ("CODCUR006","Python básico",50,36),
    ("CODCUR007","Java",150,30),
    ("CODCUR008","C#",250,50),
    ("CODCUR001","Python intermedio",50,50), #debe provocar un error UNIQUE
    ("CODCUR009","Python avanzado",75,100)
]
cursor.executemany("INSERT INTO CURSOS VALUES (NULL,?,?,?,?)", loscursos)
conexion.commit()
conexion.close()