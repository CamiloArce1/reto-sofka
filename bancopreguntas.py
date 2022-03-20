import csv

class BancoPreguntas:

    def __init__(self, nombre_archivo = '') -> None:
        self.nombre_archivo = nombre_archivo

        

    def lectura(self):  
        with open(self.nombre_archivo, encoding="utf8") as csvfile:
            self.preguntas = list(csv.DictReader(csvfile, delimiter=","))
            return self.preguntas

    def seleccion_pregunta(self, ronda, categoria ):
        
        def filtro_pregunta(pregunta):
            ronda_correcta = int(pregunta['id']) == ronda
            categoria_correcta = int(pregunta['categoria']) == categoria
            return ronda_correcta and categoria_correcta

        pregunta_seleccionada = list(filter(filtro_pregunta, self.preguntas))[0]
        return pregunta_seleccionada


        



