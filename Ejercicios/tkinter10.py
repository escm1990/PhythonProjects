#Acciones: llamar una funcion desde un boton
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
def mensaje():
    print ("Bienvenid@s")
btn1 = tkinter.Button(ventana, text="Clic aquí", command = mensaje)
btn1.pack()
ventana.mainloop()
#clic y ver terminal