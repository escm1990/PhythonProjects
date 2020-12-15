#uso de BOTH
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Python 3", bg = "red")
#BOTH = ambas
etiqueta.pack(fill = tkinter.BOTH, expand = True)
ventana.mainloop()