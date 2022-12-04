import opcion_piedra_papel_tijera_2
import opcion_adivinar_numero_3
import opcion_tirar_dados_4
import opcion_graficar_funcion_matematica_5


class Actividad_general:
    def __init__(self):
        self.inicio = 0
    def iniciar(self):
   

        while True:
                try:
                    print("Tiene a sus dispoision 4 actividades, indique que actividad desea ejecutar")
                    print("Opción 1 = Jugar a “piedra, papel, tijera” compitiendo contra la computadora.")
                    print("Opción 2 = Adivinar un número compitiendo contra la computadora.")
                    print("Opción 3 = Tirar un dado.")
                    print("Opción 4 = Grafico - Funciones Matematicas - Fases de la vida.")
                    print("Opcion 5 = Salir")
                    print("Escriba con numero la acitiviad que desea realizar")
                    print("")
                    actividad = int(input("Ingrese la opcion deseada = "))
                    print("")
                    if actividad == 1:
                        print("Usted eligió la opción 1  Jugar a “piedra, papel, tijera” compitiendo contra la computadora.")
                        juego = opcion_piedra_papel_tijera_2.Piedra_papel_tijera()
                        print("Bienvenido al PIEDRA - PAPEL - TIJEA")
                        nombre = input("Ingrese su nombre = ")
                        juego.jugador(nombre)
                        juego.jugar()
                        juego.resultado()
                        juego.resultado_final()
                        print("")
                    elif actividad == 2:
                        print("Usted eligió la opción 2 Adivinar un número compitiendo contra la computadora")
                        juego_numero = opcion_adivinar_numero_3.Adivinar_numeros()
                        print("Bienvenido al Adivine el numero")
                        nombre = input("Ingrese su nombre = ")
                        juego_numero.jugador(nombre)
                        juego_numero.jugar()
                        juego_numero.resultado()
                        juego_numero.resultado_final()
                        print("")
                    elif actividad == 3:
                        print("Usted eligió la opción 3 Tirar dados.")
                        juego_dado = opcion_tirar_dados_4.Tirar_dados()
                        print("Bienvenido la tira de de dados")
                        nombre = input("Ingrese su nombre = ")
                        juego_dado.jugador(nombre)
                        juego_dado.jugar()
                        juego_dado.puntajes()
                        juego_dado.resultado_final()
                        print("")
                    elif actividad == 4:
                        print("Usted elegió la opcion 4 Graficar una función matemática.")
                        print("Fases de la vida")
                        print("")
                        registro = opcion_graficar_funcion_matematica_5.Fases()
                        registro.ingreso()
                        registro.promedios()
                        registro.grafico()
                        print("")

                    elif actividad >= 6:
                        print("Recuerede que las opciones son del 1 al 5")
                        print("Vuelva a ingresar la opción")
                    elif actividad == 5:
                        print("Salir")
                        break

                    inicio = input("Si desea continuar con una alguna otra actividad escriba SI o S, de lo contrario cualquier presione cualquier tecla = ").lower()
                    if inicio == "si" or inicio == "s":
                        print("Se continua con actividad")
                        print("")

                    else:
                        print("No escribio SI ni tampoco la letra S")
                        print("Por lo tanto se da finalizada la actividad")
                        break
                    print("")
                except:
                    print("Solo debe ingresar numeros")
                    print("")


inicio_actividad = input("Si desea empezar con la actividad escriba SI o presione la tecla S, de lo contrario presione cualquier tecla y el programa finalizará = ").lower()
print("")
if inicio_actividad == "si" or inicio_actividad == "s":
    comenzar = Actividad_general()
    comenzar.iniciar()
else:
    print("Usted selecionó cualquier telca  .\nSe finaliza actividad")