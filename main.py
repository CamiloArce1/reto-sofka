from usuario import Usuario
from bancopreguntas import BancoPreguntas

print("***********************************")
print("**********BIENVENIDO***************")
print("***A QUIEN QUIERE SER MILLONARIO***")
print("***********************************")
participante = Usuario()
participante.registro()
participante.DatosHistoricos()
banco = BancoPreguntas('resurce/preguntas2.csv')
banco.lectura()
print(banco.seleccion_pregunta(1,3))
