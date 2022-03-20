import csv


class usuario:

    def __init__(self, nombre)-> None:
        self.nombre = nombre
        self.puntaje = 0
        self.ronda = 0
        pass

    def registro(self):
        self.nombre = input("Registre su nombre: ")
        pass
    
    def DatosHistoricos(self):
        with open ('DatosHistoricos.csv','a+',encoding='UTF8',newline='') as Historial:
            write = csv.writer(Historial)
            write.writerow([self.nombre, self.puntaje,self.ronda])
        pass


