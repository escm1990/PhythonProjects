#from indica la carpeta
#import el nombre del modulo (archivo.py)
#as es un alias para renombrar la importacion del modulo
from mis_modulos import modulo_aritmetica as mod_arit

resultado = mod_arit.sumar(2,2)
print(resultado)

resultado = mod_arit.restar(2,2)
print(resultado)

resultado = mod_arit.multiplicar(2,2)
print(resultado)

resultado = mod_arit.dividir(2,2)
print(resultado)