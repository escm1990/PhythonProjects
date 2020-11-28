'''Escriba un script que solicite al usuario digitar la contraseña para ingresar al sistema (la contraseña la debe
establecer usted por default). Si la contraseña digitada por el usuario no es la correcta deberá mostrar en pantalla
“Contraseña incorrecta ¿desea intentarlo nuevamente?” si la respuesta es si, el usuario tendrá la posibilidad de ingresar
nuevamente la contraseña, si la respuesta es no el script debe finalizar. Si la contraseña digitada es correcta deberá
mostrar en pantalla “Bienvenido al sistema”.'''

Password= input("Ingrese su contraseña: ")
Password2= "contraseña"

while Password != Password2:
    respuesta = input("Contraseña incorrecta ¿desea intentarlo nuevamente? (si/no) ")
    if respuesta == "si":
        Password= input("Ingrese su contraseña: ")
    else:
        break

if Password == Password2:
    print("Bienvenido al sistema")