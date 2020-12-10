# Va de la mano con el archivo sqlite4.py, ya que este 
# inserta en la tabla CURSOS creada en el archivo anterior
# pero sin definir el código del campo id_curso
    
import sqlite3
conexion=sqlite3.connect("AdministracionAlumnos2")
cursor = conexion.cursor()
loscursos=[
    ("Python básico",50,36),
    ("Java",150,30),
    ("C#",250,50),
    ("Python intermedio",50,50),
    ("Python avanzado",75,100)
]
cursor.executemany("INSERT INTO CURSOS VALUES (NULL,?,?,?)", loscursos)
conexion.commit()
conexion.close()