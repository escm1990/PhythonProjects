import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x400")
#establecer parámetro
def mensaje(participante):
    print ("Bienvenid@ " + participante)
#enviando argumento
#lambda para funciones con parámetros o definir funciones cortas a utilizar una vez
btn1 = tkinter.Button(ventana, text="Clic aquí", command = lambda: mensaje("Francisco Quezada"))
btn1.pack()
ventana.mainloop()
#clic y ver terminal