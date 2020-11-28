#Desarrollado por Erick Stanley Cruz Martínez - GRUPO 4

nombre = input("Ingrese su nombre: ")
dui = input("Ingrese su DUI: ")
nit = input("Ingrese su NIT: ")

sueldo = float(input("Ingrese su sueldo: "))
bono = float(input("Ingrese su bono: "))
sueldoAsignar = 0

if bono > 0:
    sueldoAsignar = sueldo + bono
else:
    sueldoAsignar = sueldo

sueldoBruto = sueldoAsignar

if sueldoBruto > 1000:
    isss = 30
else:
    isss = sueldoBruto*0.03

if sueldoBruto > 7028.29:
    afp = 509.55
else:
    afp = sueldoBruto*0.0725

sueldoDeduc1 = sueldoBruto-(isss+afp)

renta = sueldoDeduc1*0.10

descuentoTotal = round(isss+afp+renta,2)

salarioneto = round(sueldoAsignar-descuentoTotal,2)

print("Nombre: {}\nDUI: {}\nNIT: {}\nDescuento Total: {}\nSalario Neto: {}".format(nombre,dui,nit,descuentoTotal,salarioneto))