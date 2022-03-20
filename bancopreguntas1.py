import pandas as pd

class Preguntas:

    def __init__(self,nombre='',ronda=0,categoria=0):
        self.nombre = nombre
        self.ronda = ronda
        self.categoria = categoria
        pass
    
    def lectura(self):
        self.nombre = 'resurce/preguntas2.csv'
        self.categoria = 0
        self.ronda = 1 
        preguntas = pd.read_csv(self.nombre, header='0')
        print(preguntas.iloc(self.ronda))

