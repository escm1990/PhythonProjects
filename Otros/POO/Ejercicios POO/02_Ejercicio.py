# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando 
# el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar 
# un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():

    def __init__(self,valor1,valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        res = self.valor1 + self.valor2
        print("Suma: ",res)

    def restar(self):
        res = self.valor1 - self.valor2
        print("Resta: ",res)

    def multiplicar(self):
        res = self.valor1 * self.valor2
        print("Multiplicación: ",res)
    
    def dividir(self):
        if(self.valor2 > 0):
            res = self.valor1 / self.valor2
            print("Dividir: ",res)
        else:
            print("No se puede dividir entre cero")

###################################################

calc = Calculadora(2,2)
calc.sumar()
calc.restar()
calc.multiplicar()
calc.dividir()