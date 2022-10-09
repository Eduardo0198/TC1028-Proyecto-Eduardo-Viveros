("####### PROYECTO TC1028 ########")
import os

#================== Variables Globales  =======================================
global lista
lista=[]

#================== funciones auxiliares  =======================================

def valor_preguntas (entrada):

 if entrada == "1":
    res = 10
 elif entrada == "2":
    res = 20
 elif entrada == "3":
    res = 30

 return res 
   
def contador_respuestas(respuestas):
   global lista
   lista.append(respuestas)       
   print("Tu resultado es: \t", lista)
   return lista

def total ():
   global lista
   total=0
   for i in lista:
      total=total+i
   
   print("\t (⌐■_■) El total de puntos es: \t", total)
   return total

#==================Funcion Auxiliar==================

def pausa ():
    reset = input("Presiona cualquier boton para pasar a la siguiente pregunta (☞ﾟヮﾟ)☞")
    os.system("cls")

#==================Parte principal del programa==================

print("BIENVENIDO AL")
print("\n\t\t\t(*￣3￣) ANALIZADOR DE CARRERAS\t( ͡° ͜ʖ ͡°)")
print("\n\n(★‿★) DONDE TE ORIENTAREMOS A DECIDIR CUAL ES LA MEJOR CARRERA PARA TI POR FAVOR CONTESTA LAS SIGUIENTES PREGUNTAS (●'◡'●)\n\n")


pregunta_1 = input("Pregunta 1: \nDe las siguientes materias ¿Cual es tu favorita?: \n\n\t\t1. Matematicas-Fisica\n\t\t2. Computacion\n\t\t3. Quimica\n\nRespuesta: ")
os.system("cls")
while pregunta_1 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_1=input("Pregunta 1: \nDe las siguientes materias ¿Cual es tu favorita?: \n\n\t\t1. Matematicas-Fisica\n\t\t2. Computacion\n\t\t3. Quimica\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_1))
pausa()

pregunta_2 = input("Pregunta 2: \nPara ti ¿Que es la ingenieria?: \n\n\t1. Es el poder crear cosas atarves de la indrustria\n\n\t2. Es el saber como funcionan los aparatos electronicos por dentro\n\n\t3. Es el poder crear soluciones a porblemas atraves de un laboratorio \n\nRespuesta: ")
os.system("cls")
while pregunta_2 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_2 = input("Pregunta 2: \nPara ti ¿Que es la ingenieria?: \n\n\t1. Es el poder crear cosas atarves de la indrustria\n\n\t2. Es el saber como funcionan los aparatos electronicos por dentro\n\n\t3. Es el poder crear soluciones a porblemas atraves de un laboratorio \n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_2))
pausa()

pregunta_3 = input(f"pregunta 3: ¿Cual crees que sea tu mejor fortaleza?: \n\n\t1. Analisis\n\n\t2. Control bajo estres\n\n\t3. Trabajo en equipo\n\nRespuesta: " )
os.system("cls")
while pregunta_3 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_3 = input(f"pregunta 3: ¿Cual crees que sea tu mejor fortaleza?: \n\n\t1. Analisis\n\n\t2. Control bajo estres\n\n\t3. Trabajo en equipo\n\nRespuesta: " )
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_3))
pausa()

pregunta_4 = input("pregunta 4: ¿En que area Ingenieril te gustaria desempeñarte?: \n\n\t1. Mecatronica y Robotica\n\n\t2. Tecnologias Computacionales\n\n\t3. Bioingenierias\n\nRespuesta: ")
os.system("cls")
while pregunta_4 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_4 = input("pregunta 4: ¿En que area Ingenieril te gustaria desempeñarte?: \n\n\t1. Mecatronica y Robotica\n\n\t2. Tecnologias Computacionales\n\n\t3. Bioingenierias\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_4))
pausa()

pregunta_5 = input("pregunta 5: Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas?: \n\n\t- 1\n\n\t- 2\n\n\t- 3 \n\nRespuesta: ") 
os.system("cls")
while pregunta_5 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_5 = input("pregunta 5: Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas?: \n\n\t- 1\n\n\t- 2\n\n\t- 3 \n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_5))
pausa()

pregunta_6 = input("pregunta 6: ¿En que tipo de industria te ves trabajando en un futuro?: \n\n\t1. Manufactura y diseño mecanico\n\n\t2. Big TECH\n\n\t3. Aeroespacial\n\nRespuesta: ")
os.system("cls")
while pregunta_6 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_6 = input("pregunta 6: ¿En que tipo de industria te ves trabajando en un futuro?: \n\n\t1. Manofuctura y diseño mecanico\n\n\t2. Big TECH\n\n\t3. Aeroespacial\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_6))
pausa()

pregunta_7 = input("pregunta 7: ¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso?: \n\n\t1. Analitico\n\n\t2. Creativo\n\n\t3. Ingenioso\n\nRespuesta: ")
os.system("cls")
while pregunta_7 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_7 = input("pregunta 7: ¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso?: \n\n\t1. Analitico\n\n\t2. Creativo\n\n\t3. Ingenioso\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_7))
pausa()

pregunta_8 = input(f"pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t1. Visual\n\n\t2. Emocional\n\n\t3. Asociativo\n\nRespuesta: ")
os.system("cls")
while pregunta_8 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_8 = input(f"pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t1. Visual\n\n\t2. Emocional\n\n\t3. Asociativo\n\nRespuesta: ")
   os.system("cls")



contador_respuestas(valor_preguntas(pregunta_8))
pausa()

total()