#creacion de objetos (widgets), ej. un label
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Curso de Python 3")
#etiqueta.pack() #método pack muestra en pantalla (centrado por defecto)
etiqueta.pack(side=tkinter.BOTTOM) #side = lado
#etiqueta.pack(side=tkinter.RIGHT)
ventana.mainloop()
#No se mostrará el Label