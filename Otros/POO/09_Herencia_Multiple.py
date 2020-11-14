class claseA():
    def mensaje(self):
        print("Esta es la clase A")
    def primera(self):
        print("Estas dentro de la clase A")

class claseB():
    def mensaje(self):
        print("Esta es la clase B")
    def segunda(self):
        print("Estas dentro de la clase B")

class claseC(claseA,claseB): ##toma como primaria la clase más a la izquierda
    pass

objetoC = claseC()
objetoC.primera()
objetoC.segunda()