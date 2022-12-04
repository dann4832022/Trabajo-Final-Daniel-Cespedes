import matplotlib.pyplot as plt
# ● Graficar una función matemática.
class Fases():
    def __init__(self):
        self.primeraInfanacia = 0
        self.ninezTemprana = 0
        self.ninezIntermedia = 0
        self.adolescencia = 0
        self.juventud = 0
        self.madurez = 0
        self.adultezMadura = 0
        self.terceraEdad = 0
        self.totalEncuestados = 0
        self.promediosPrimeraInfancia = 0
        self.promediosNinezTemprana  = 0
        self.promediosNinezIntermedia = 0
        self.promediosAdolescencia = 0
        self.promediosJuventud = 0
        self.promediosMadurez = 0
        self.promediosAdultezMadura = 0
        self.promediosTerceraEdad = 0
    
    def ingreso(self):
        print("Registro de edades\nComenzar")
        print("")        
        while True:
            try:
                edad = int(input("Edad = "))
                self.totalEncuestados += 1
                if edad >= 0 and edad <= 2:
                    self.primeraInfanacia +=1
                        
                elif edad >= 3 and edad <=6:
                    self.ninezTemprana+=1
                    
                elif edad >=7 and edad <= 11:
                    self.ninezIntermedia +=1
                    
                elif edad >= 12 and edad <=17:
                    self.adolescencia +=1
                    
                elif edad >= 18 and edad <= 35:
                    self.juventud +=1

                elif edad >= 36 and edad <=50:
                    self.madurez +=1
                
                elif edad >=51 and edad <= 65:
                    self.adultezMadura +=1
                
                elif edad >=66 and edad <= 999:
                    self.terceraEdad +=1
            except:
                print("Solo puede ingresar numeros")
            print("")
            print("Si desea finalizar presione X, sino presione cualquier letra")    
            continuar = input("Continuar = ").lower()
            if continuar == "x":
                break
            print("")
            
    def promedios(self):
        print("Total")
        print(self.totalEncuestados)
        print("")
        print("Primera Infancia")
        print(self.primeraInfanacia)
        self.promediosPrimeraInfancia = round(self.primeraInfanacia * 100 / self.totalEncuestados, 2)
        print(self.promediosPrimeraInfancia)
        print("")
        print("Niñez Temprana")
        print(self.ninezTemprana)
        self.promediosNinezTemprana =  round(self.ninezTemprana * 100 / self.totalEncuestados, 2)
        print(self.promediosNinezTemprana)
        print("")
        print("Niñez Intermedia")
        print(self.ninezIntermedia)
        self.promediosNinezIntermedia =  round(self.ninezIntermedia * 100 / self.totalEncuestados, 2)
        print(self.promediosNinezIntermedia)
        print("")
        print("Adolescencia")
        print(self.adolescencia)
        self.promediosAdolescencia =  round(self.adolescencia * 100 / self.totalEncuestados, 2)
        print(self.promediosAdolescencia)
        print("")
        print("Juventud")
        print(self.juventud)
        self.promediosJuventud =  round(self.juventud * 100 / self.totalEncuestados, 2)
        print(self.promediosJuventud)
        print("")
        print("Madurez")
        print(self.madurez)
        self.promediosMadurez =  round(self.madurez * 100 / self.totalEncuestados, 2)
        print(self.promediosMadurez)
        print("")
        print("Adultez Madura")
        print(self.adultezMadura)
        self.promediosAdultezMadura =  round(self.adultezMadura * 100 / self.totalEncuestados, 2)
        print(self.promediosAdultezMadura)    
        print("")
        print("Tercera Edad")
        print(self.terceraEdad)
        self.promediosTerceraEdad =  round(self.terceraEdad * 100 / self.totalEncuestados, 2)
        print(self.promediosTerceraEdad)
        print("")
    def grafico(self):
        fig, ax = plt.subplots()
        x = (["Primera Infancia", "Niñez Temprana", "Niñez Intermedia", "Adolescencia", "Juventud" , "Madurez", "Adultez Madura", "Tercera Edad"])
        y = ([self.promediosPrimeraInfancia, self.promediosNinezTemprana, self.promediosNinezIntermedia, self.promediosAdolescencia, self.promediosJuventud, self.promediosMadurez, self.promediosAdultezMadura, self.promediosTerceraEdad])
        bar_labels = (['red', 'blue', '_red', 'orange','red', 'blue', '_red', 'orange'])
        bar_colors =(['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red', 'tab:blue', 'tab:red', 'tab:orange'])
        ax.bar(x, y, label=bar_labels, color=bar_colors)
        ax.set_ylabel('Porcentajes %')
        ax.set_xlabel("Fases de la vida")
        ax.set_title(f"Las 8 fases de la vida en porcentajes.\nTotal personas encuestadas = {self.totalEncuestados}")
        plt.show()     


