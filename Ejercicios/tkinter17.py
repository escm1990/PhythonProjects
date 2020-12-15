import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
captura_texto = tkinter.Entry(ventana, font = "Arial 15")
captura_texto.pack()
ellabel = tkinter.Label(ventana)
ellabel.pack()
def capturaeltexto():
    eltexto = captura_texto.get()
    ellabel["text"] = eltexto
btn1 = tkinter.Button(ventana, text = "Enviar texto", command = capturaeltexto)
btn1.pack()
ventana.mainloop()