import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos")
cursor = conexion.cursor()

#instrucción en varias líneas
cursor.execute('''
    CREATE TABLE CURSOS (
    codigo_curso VARCHAR(4) PRIMARY KEY,
    nombre_curso VARCHAR(50),
    cupos_curso INTEGER,
    horas_curso INTEGER)
    '''
)
 
loscursos=[
    ("CI01","Python básico",50,36), #CI01 campo clave
    ("CI02","Java",150,30),
    ("CI03","C#",250,50),
    ("CI04","Python intermedio",50,50),
    ("CI05","Python avanzado",75,100)
]
cursor.executemany("INSERT INTO CURSOS VALUES (?,?,?,?)", loscursos)
conexion.commit()

#Lo insertar porque no existe
cursor.execute("INSERT INTO CURSOS VALUES ('CI06','PHP',60,100)")

#No lo inserta porque ya existe
cursor.execute("INSERT INTO CURSOS VALUES ('CI04','JS',40,50)")

conexion.close()