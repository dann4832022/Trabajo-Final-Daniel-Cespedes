import random
# ● Adivinar un número compitiendo contra la computadora.
class Adivinar_numeros():
    def __init__(self):
        self.rondas = 0
        self.victoria_maquina = 0
        self.victoria_humano = 0
        self.empate = 0
        self.nombre_jugador = ""
    
        print("Estamos por jugar")

    def jugador(self, nombre):
        self.nombre_jugador = nombre
        print(f"{nombre} vs Maquina")

    def jugar(self):
        print("")
        print("Intente advinar el numero que elegira la maquina.\nTiene que ser un numero del 0 al 5")
        while True:
            try:
                jugador_1 = int(input("Ingres el numero =  "))
                if jugador_1 >= 6:
                    print("Recuerda que solo debes ingresar un numero del 1 al 5\nEsta jugada no cuenta como ronda")
                    continue
                print("")   
                maquina = random.randint(0, 5)
                print(f"La maquina seleccionó el numero {maquina}")
            
                if jugador_1 == maquina:
                    print("Has acertado, elegiste el mismo numero que la maquina")
                    self.victoria_humano = self.victoria_humano + 1
                    self.rondas = self.rondas + 1
                    print("")
                elif jugador_1 < maquina or jugador_1 > maquina:
                    print("Game Over")
                    self.victoria_maquina = self.victoria_maquina + 1
                    self.rondas = self.rondas + 1
                    print("")
            except:
                print("Solo puede ingresar numeros")
                print("")
            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break
            print("")
    def resultado(self):
        print(f"Se han jugado un total de {self.rondas} rondas")
        print("")
        print(f"{self.nombre_jugador} has tenido un total de {self.victoria_humano} partida/s ganadas")
        print("")
        print(f"La maquina ha obenido un total de  {self.victoria_maquina} partida/s ganadas")
        print("")

    def resultado_final(self):
        if self.victoria_humano > self.victoria_maquina:
            print(f"{self.nombre_jugador} eres el ganador final!!\nFFELICIDADES!!\Hasta la proxima revancha!!")
            print("")
        elif self.victoria_maquina > self.victoria_humano:
            print(f"La maquina ha sido el ganador final!!\nHasta la proxima revancha!!!")
            print("")
        elif self.victoria_humano == self.victoria_maquina:
            print("Se ha producido un empate")
        print("")

