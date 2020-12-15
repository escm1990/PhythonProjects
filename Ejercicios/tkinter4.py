#uso de propiedad bg
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Python 3", bg = "blue")
etiqueta.pack(side=tkinter.BOTTOM)
ventana.mainloop()