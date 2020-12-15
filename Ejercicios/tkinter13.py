import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
btn1 = tkinter.Button(ventana, text="Clic aquí", command = lambda: print("TKINTER"))
btn1.pack()
ventana.mainloop()