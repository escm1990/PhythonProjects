import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
def mensaje():
    print ("Bienvenid@s")
btn1 = tkinter.Button(ventana, text="Clic aquí", command = mensaje())
#al colocar () en la función se ejecuta automaticamente la función
btn1.pack()
ventana.mainloop()
#clic y ver terminal