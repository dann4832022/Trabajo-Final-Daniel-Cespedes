import random
# ● Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
class Piedra_papel_tijera:
    def __init__(self):
        self.rondas = 0
        self.victoria_maquina = 0
        self.victoria_humano = 0
        self.empate = 0
        self.nombre = ""

        
    def jugador(self, nombre):
        self.nombre = nombre
        print(f"{nombre} vs Maquina")

    def jugar(self):
        print("")
        while True:
            
            jugador_1 = input("Escriba la opción deseada\nOpción 1= Piedra \nOpción 2= Papel \nOpción 3= Tijera\nSeleccione la opción = ").lower()

            maquina = random.choice(["piedra", "papel", "tijera"])
            self.rondas = self.rondas + 1            
            #Primera arte = el jugador elige la opción papel
            if jugador_1 == "papel" and maquina == "papel":
                print(f"Empate!!!\nAmbos jugadores elegieron Papel")
                self.empate = self.empate + 1
                print("")
            elif jugador_1 == "papel" and maquina == "tijera":
                print(f"{self.nombre} eligió papel y la maquina eligió tijera.\nGanador Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            elif jugador_1 == "papel" and maquina == "piedra":
                print(f"{self.nombre} papel y la maquina eligió piedra.\nGanador {self.nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")

            # Segunda parte = El jugador elige la opción piedra
            elif jugador_1 == "piedra" and maquina == "papel":
                print(f"{self.nombre} eligio piedra y la maquina eligio papel.\nGanador = Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "tijera":
                print(f"{self.nombre} eligió piedra y la maquina eligió tijera.\nGanador {self.nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "piedra":
                print(f"Empate!!!\nAmbos jugadores elegieron Piedra")
                self.empate = self.empate + 1

            # Tercera parte = el jugador elige la opción tijera
            elif jugador_1 == "tijera" and maquina == "tijera":
                print(f"Empate!!!\nAmbos jugadores elegieron Tijera")
                self.empate = self.empate + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "papel":
                print(f"{self.nombre} eligió tijera y la maquina eligió papel.\nGanador {self.nombre}")
                self.victoria_humano = self.victoria_humano + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "piedra":
                print(f"{self.nombre} eligió papel y la maquina eligió piedra.\nGanador Maquina")
                self.victoria_maquina = self.victoria_maquina + 1
                print("")
            # continuar o finalizar

            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break
            print("")

    def resultado(self):
        print(f"Se han jugado un total de {self.rondas} rondas")
        print("")
        print(f"{self.nombre} has tenido un total de {self.victoria_humano} partida/s ganadas")
        print("")
        print(f"La maquina ha obenido un total de  {self.victoria_maquina} partida/s ganadas")
        print("")
        print(f"Hubo un total de {self.empate} partida/s que terminaron en empates")
        print("")

    def resultado_final(self):
        if self.victoria_humano > self.victoria_maquina and self.victoria_humano > self.empate:
            print(f"{self.nombre} eres el ganador final!!\nFFELICIDADES!!\nHasta la proxima revancha!!")
            print("")
        elif self.victoria_maquina > self.victoria_humano and self.victoria_maquina > self.empate:
            print(f"La maquina ha sido el ganador final!!\nHasta la proxima revancha!!!")
            print("")
        elif self.empate > self.victoria_maquina and self.empate > self.victoria_humano:
            print(f"Se ha producido un empate tecnico.\nHasta la proxima revancha!!")
            print("")
        elif self.victoria_humano == 0 and self.victoria_maquina == 0 and self.empate == 0:
            print("No se ha jugado ninguna partida")
            print("")        
        elif self.victoria_humano == self.empate and self.victoria_maquina == self.empate:
            print("Felicitaciones, has sido el ganado por definición")
            print("")

