#CLAUSULA UNIQUE: Impide que la información de un campo se repita en la BD

import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos3")
cursor = conexion.cursor()
cursor.execute('''
    CREATE TABLE CURSOS (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_curso VARCHAR(10) UNIQUE,
    nombre_curso VARCHAR(50),
    cupos_curso INTEGER,
    horas_curso INTEGER)
    '''
)

loscursos=[
    ("CODCUR001","Python básico",50,36),
    ("CODCUR002","Java",150,30),
    ("CODCUR003","C#",250,50),
    ("CODCUR004","Python intermedio",50,50),
    ("CODCUR005","Python avanzado",75,100)
]
cursor.executemany("INSERT INTO CURSOS VALUES (NULL,?,?,?,?)", loscursos)
conexion.commit()
conexion.close()