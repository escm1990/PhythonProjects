#uso de fill
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Python 3", bg = "red")
etiqueta.pack(fill = tkinter.X)#fill = llenar
ventana.mainloop()