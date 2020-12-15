'''
total=0
nro=int(input("Número: "))
while nro != 0:
    total += nro
    nro =int(input("Numero: "))
    '''

'''
variable1 = (1,9,6,0,2,5,23,8.9,True)
variable2 = variable1.index(5)
print(variable2)
'''
'''
import tkinter
ventana = tkinter.Tk()
ventana.geometry("450x600")
captura = tkinter.Entry(ventana)
captura.pack()
ventana.mainloop
'''

'''
import sqlite3
conexion = sqlite3.connect("EvaluacionFinal")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE ALUMNOS(nombre_alumno VARCHAR(50), edad_alumno INTEGER, nombre_curso VARCHAR(50))")
cursor.execute("INSERT INTO ALUMNOS VALUES ('Francisco Quezada',33,'Python 3')")
conexion.commit()
'''

'''
import sqlite3
conexion = sqlite3.connect("EvaluacionFinal")
cursor = conexion.cursor()
lista = [
    ("Laura",20,"Java"),
    ("Juan",30,"Python"),
    ("Francisco",45,"C#")
]
cursor.executemany("INSERT INTO ALUMNOS VALUES (?,?,?)",lista)
conexion.commit()
'''
'''
import sqlite3
conexion = sqlite3.connect("EvaluacionFinal")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM ALUMNOS")
lista = cursor.fletchall

for alumno in lista:
    print(alumno)

conexion.commit()
'''
'''
lista_participantes=["Francisco","Luis","Ana",10,"Carlos","Juan",False]

lista_participantes.extend(["Ernesto","Fátima","Ruth","Pedro"])

lista_participantes.remove("Fátima")

print("Fátima" in lista_participantes)

print(lista_participantes)
'''
'''
eltexto = "Python es una gran onda"
print(len(eltexto))
'''

def calcula_area(base,altura):

    '''

    >>> calcula_area(10,5)
    25.1

    '''

    return (base*altura)/2

import doctest
doctest.testmod()