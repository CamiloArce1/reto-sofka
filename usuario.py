import csv


class Usuario:

    def __init__(self)-> None:
        self.nombre = None
        
        

    def registro(self):
        self.nombre = input("Registre su nombre: ")
        return self.nombre
    
    def DatosHistoricos(self):
        with open ('DatosHistoricos.csv','a+',encoding='UTF8') as Historial:
            write = csv.writer(Historial)
            write.writerow([self.nombre])
        


