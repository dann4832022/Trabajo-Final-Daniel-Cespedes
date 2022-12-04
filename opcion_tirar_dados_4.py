import random
# ● Tirar un dado.
class Tirar_dados():

    def __init__(self):
      
        self.dado_1 = 0
        self.dado_2 = 0
        self.numero_minimo = 1
        self.numero_maximo = 6
        self.rondas = 0
        self.victorias = 0
        self.perdida = 0
        self.nombre = ""

    def jugador(self,nombre):
        self.nombre = nombre
        print(nombre)

    
    def jugar(self):
        while True:
            tirar_dados = input("Deseas tirar los dados SI/NO == ").lower()
            print("")
            if tirar_dados == "no" or tirar_dados == "n":
                break
            self.dado_1 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_1)
            self.dado_2 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_2)
            self.rondas = self.rondas + 1
            if self.dado_1 == self.dado_2:
                print("Los numeros de ambos dados son iguales.\nFelicidades.\nHas ganado la partida")
                self.victorias = self.victorias + 1

            elif self.dado_1 != self.dado_2:
                print("No coincidien los numeros.\nHas perdido la partida.")
                self.perdida = self.perdida + 1
            print("")

    def puntajes(self):
        print(f"Se han judado un total de {self.rondas}")
        print("")
        print(f"{self.nombre} has ganado un total de {self.victorias} partidas!!..")
        print("")
        print(f"{self.nombre} has perdido un total de {self.perdida} partidas!!..")
        print("")
    def resultado_final(self):
        if self.victorias > self.perdida:
            print(f"Eres el ganador final del juego")
            print("")
        elif self.victorias < self.perdida:
            print(f"Has perdido mas veces de las que has ganado. Sigue intentando")
            print("")
        elif self.victorias == self.perdida:
            print("Se ha producido un empate, has ganado y perdido las mismmas cantidad de veces.\nAimate a la revancha")
        print("")
