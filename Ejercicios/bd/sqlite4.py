import sqlite3

conexion=sqlite3.connect("AdministracionAlumnos2")

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE CURSOS (
    id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_curso VARCHAR(50),
    cupos_curso INTEGER,
    horas_curso INTEGER)
    '''
    )

loscursos=[
        ("Python básico",50,36), #eliminanos el dato del campo 1
        ("Java",150,30),
        ("C#",250,50),
        ("Python intermedio",50,50),
        ("Python avanzado",75,100)
        ]

#Sustituir el primer valor de VALUES por NULL
cursor.executemany("INSERT INTO CURSOS VALUES (NULL,?,?,?)", loscursos)
conexion.commit()

conexion.close()