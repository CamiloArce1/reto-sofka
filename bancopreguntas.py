import csv

class BancoPreguntas:

    def __init__(self,nombreArchivo='') -> None:
        self.nombreArchivo = nombreArchivo
        pass

    def lectura(self):  
        self.nombreArchivo = 'resurce/preguntas2.csv'
        with open(self.nombreArchivo, encoding="utf8") as csvfile:
            preguntas = csv.DictReader(csvfile, delimiter=",")
            for row in preguntas:
             print(row)
            
        pass
preguntas1=BancoPreguntas()


