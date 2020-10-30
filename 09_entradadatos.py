print("Hola, ¿cuál es tu nombre?")
nombre = input() #captura la informacion del teclado
print("Hola",nombre) #concatenando texto y variable
print("Digita tu edad:")
edad = int(input()) #la funcion int convierte un string en entero
print("Tu edad es:",edad)
print("Digita un numero decimal")
promedio = float(input())
print("El numero ingresado es",promedio)
print("¿Eres de este grupo (si/no)?")
respuesta = input()=="si"
print("Bienvenido",respuesta)