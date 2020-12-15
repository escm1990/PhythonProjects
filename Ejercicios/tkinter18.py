#uso de grid
import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
btn1 = tkinter.Button(ventana, text = "Enviar", width = 10, height = 1)
caja1 = tkinter.Entry(ventana, font = "Arial 15")
btn2 = tkinter.Button(ventana, text = "Borrar", width = 10, height = 2)
texto1 = tkinter.Label(ventana, text = "Python 3")
texto1.grid(row = 0, column = 0)
caja1.grid(row = 1, column = 0)
btn1.grid(row = 1, column = 1)
btn2.grid(row = 2, column = 0)
ventana.mainloop()