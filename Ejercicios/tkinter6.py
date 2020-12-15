#uso de expand
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
etiqueta = tkinter.Label(ventana, text = "Python 3", bg = "red")
#etiqueta.pack(fill = tkinter.Y, expand = True)
#etiqueta.pack(fill = tkinter.X, expand = True)
etiqueta.pack(fill = tkinter.Y, expand = 1) #1 puede usarse tanto True como 1
ventana.mainloop()