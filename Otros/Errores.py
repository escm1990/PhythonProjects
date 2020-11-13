# Una manera de validar que HASTA que el usuario no se equivoque con el ingreso de la edad es haciendo uso de WHILE - BREAK

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es:",edad)
        break
    except:
        print("Ingresaste un valor erróneo")   
    finally:
        print("La ejecución ha finalizado")             