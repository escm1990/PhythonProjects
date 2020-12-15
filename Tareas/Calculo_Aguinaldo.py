# SCRIPT DESARROLLADO POR:
# ERICK STANLEY CRUZ MARTÍNEZ
# GRUPO 4

'''
Desarrolle un script en el cual el usuario (contador de una empresa) pueda introducir los siguientes datos:

-Nombre del empleado
-DUI del empleado
-NIT del empleado
-Sueldo neto del empleado
-Tiempo que el empleado lleva trabajando en la empresa (usted puede elegir si el usuario debe digitar años, meses o días)
-Calcule el aguinaldo que le corresponde recibir en base a la información proporcionada en el siguiente link: 
 https://www.mtps.gob.sv/temas/aguinaldo/
-Si considera que el usuario debe proporcionar información adicional a la que se solicita puede adicionarla.
-Imprima el aguinaldo a recibir y la información proporcionada por el usuario.
-Usted puede elegir si su aplicación será en consola o con interfaz gráfica.
'''
#importando interfaz gráfica
import tkinter as tk

#función para cálculo de aguinaldo
def calculaAguinaldo():
    
    #obteniendo valores de los widgets
    cajasueldo = sueldo.get()
    cajatiempo = tiempo.get()
    cajanombre = nombre.get()
    cajaDUI = dui.get()
    cajaNIT = nit.get()

    #definiendo variables
    elsueldo = float(cajasueldo)
    eltiempo = float(cajatiempo)
    aguinaldo = 0
    diasCalculo = 0
    esProporcional = False
    salarioDiario = 0
    
    #calculando el salario diario
    salarioDiario = elsueldo/30

    '''
    1° De 1 año y menos de 3 años de servicio, se calculara con un salario equivalente a 15 días;
    2° De 3 años a menos de 10 años de servicio, se calculara con un salario equivalente a 19 días;
    3° De 10 años o más de servicio, se calculara con un salario equivalente a 21 días.
    '''
    
    if(eltiempo >= 365 and eltiempo <=365*3):
        print("El empleado tiene entre 1 y 3 años")
        diasCalculo = 15
    elif(eltiempo >= 365*3 and eltiempo <=365*10):
        print("El empleado tiene entre 3 y 10 años")
        diasCalculo = 19
    elif(eltiempo > 365*10):
        print("El empleado tiene más de 10 años")
        diasCalculo =  21
    else:
        print("El empleado no tiene el año cumplido")
        diasCalculo = 15
        esProporcional = True

    print("Dias Cálculo: "+str(diasCalculo))

    #calculando aguinaldo
    if(esProporcional):
        aguinaldo = round(salarioDiario*diasCalculo*eltiempo/365,2)
    else:
        aguinaldo =  round(salarioDiario*diasCalculo,2)

    label6["text"] = "Nombre: "+cajanombre+"\nDUI: "+cajaDUI+"\nNIT: "+cajaNIT+"\nDías laborados: "+cajatiempo+"\n Aguinaldo resultante: $"+str(aguinaldo)   

#creando contenedor (ventana)
ventana = tk.Tk()   
ventana.geometry("325x250")
ventana.title("Calculadora de Aguinaldo")

#creando los widgets (controles)
label1 = tk.Label(ventana, text = "Nombre: ")
nombre = tk.Entry(ventana, font = "Arial 12",)
label2 = tk.Label(ventana, text = "DUI: ", )
dui = tk.Entry(ventana, font = "Arial 12")
label3 = tk.Label(ventana, text = "NIT: ")
nit = tk.Entry(ventana, font = "Arial 12")
label4 = tk.Label(ventana, text = "Sueldo: ")
sueldo = tk.Entry(ventana, font = "Arial 12", justify="right")
label5 = tk.Label(ventana, text = "Tiempo en días: ")
tiempo = tk.Entry(ventana, font = "Arial 12", justify="right")
label6 = tk.Label(ventana, height = 5)
btn = tk.Button(ventana, text = "Calcular", width = 10, height = 1, command = calculaAguinaldo)

#ubicando los componentes
label1.grid(row = 0, column = 0)
nombre.grid(row = 0, column = 1)
label2.grid(row = 1, column = 0)
dui.grid(row = 1, column = 1)
label3.grid(row = 2, column = 0)
nit.grid(row = 2, column = 1)
label4.grid(row = 3, column = 0)
sueldo.grid(row = 3, column = 1)
label5.grid(row = 4, column = 0)
tiempo.grid(row = 4, column = 1)
btn.grid(row = 5, column = 0)
label6.grid(row = 5, column = 1)

#mostrando el contenedor
ventana.mainloop()