("####### PROYECTO TC1028 ########")
import os

#================== Variables Globales  ===============================
"""
Defino una lista global para poder tener libertidad a la hora de ocupar-
la en varias funciones
"""
global lista
lista=[]
global lista_pregntas
lista_preguntas=[]
#================== funciones auxiliares  =============================
"""
Defini varias funciones que estaria ocupando a lo largo de todo mi codi-
go, al ser un test con varias preguntas el proceso de estas se repetiria, 
de esta manera siento que es mejor hacer funciones con instrucciones mas 
generales para que la funcion aplique co distintos parametros
"""
def valor_preguntas (entrada):

 if entrada == "1":
    res = 10
 elif entrada == "2":
    res = 20
 elif entrada == "3":
    res = 30

 return res 

"""
La funcion valor_preguntas le asigna un valor a cada respuesta dependien-
do que string reciba
"""

def contador_respuestas(respuestas):
   global lista
   lista.append(respuestas)       
   print("Tu resultado es: \t", lista)
   return lista
"""
La funcion contador_respuestas se encarga de meter los valores de las res-
puestas, adjunta todos esos valores en un lista global (esta la ocupe para
tener una misma  variable que pueda ocupar en diferentes funciones), a es-
ta solo le agregue .append para agregar los valores de la funcion pasada, 
aparte de que esta te va mostrando el valor de la respuesta que hayas metido.
"""
def total ():
   global lista
   total=0
   for i in lista:
      total=total+i
    
   print("\t (⌐■_■) El total de puntos es: \t", total)
   return total

"""
La funcion total se encarga de sumar los valores de la lista global, suma 
estos elemtos atraves de un ciclo for y un acumulador, para que al final
te indique cual es tu resultado final.
"""

#==================Funcion Auxiliar==================

def pausa ():
    reset = input("Presiona cualquier boton para pasar a la siguiente pregunta (☞ﾟヮﾟ)☞")
    os.system("cls")

"""
La funcion pausa solo es un pequeño intermedio entre pregunta y pregunta
"""

#==================Cuerpo del programa==================

print("\n\t\t\t\t\tBIENVENIDO AL")
Nombre_del_proyecto = ("\n\t\t\t(*￣3￣) analizador de ingenierias\t( ͡° ͜ʖ ͡°)")
print(Nombre_del_proyecto.upper())
print("\n\n(★‿★) DONDE TE ORIENTAREMOS A DECIDIR CUAL ES LA MEJOR CARRERA PARA TI POR FAVOR CONTESTA LAS SIGUIENTES PREGUNTAS (●'◡'●)\n\n")


pregunta_1 = input("Pregunta 1: \nDe las siguientes materias ¿Cual es tu favorita?: \n\n\t\t1. Matematicas-Fisica\n\t\t2. Computacion\n\t\t3. Quimica\n\nRespuesta: ")
os.system("cls")
while pregunta_1 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_1=input("Pregunta 1: \nDe las siguientes materias ¿Cual es tu favorita?: \n\n\t\t1. Matematicas-Fisica\n\t\t2. Computacion\n\t\t3. Quimica\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_1))

pausa()
"""
En esta parte el While crea un ciclo que te regresa a la misma pregunta si 
es que no se cumple la condicion.
Abajo del while se ve como invoco las funciones anteriormente definidas para
poder ir acumulando los valores de las respuestas en la lista global y abajo
de esa la funcion pausa para dar el intermedio entre pregunta y pregunta
(Este mismo proceso se repetira con las 13 preguntas que conforman al test)

"""
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

pregunta_8 = input("pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t1. Visual\n\n\t2. Emocional\n\n\t3. Asociativo\n\nRespuesta: ")
os.system("cls")
while pregunta_8 >= "4":
   print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
   pregunta_8 = input("pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t1. Visual\n\n\t2. Emocional\n\n\t3. Asociativo\n\nRespuesta: ")
   os.system("cls")

contador_respuestas(valor_preguntas(pregunta_8))
pausa() 

pregunta_9 = input("pregunta 9: ¿Sientes interes por la electronica y los componentes de las maquinas?: \n\n\t1. Es algo que me encanta \n\n\t2. Me llama la atencion \n\n\t3. No me interesa \n\nRespuesta: ")
os.system("cls")
while pregunta_9 >= "4":
    print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
    os.system("cls")

contador_respuestas(valor_preguntas(pregunta_9))
pausa()

pregunta_10 = input("pregunta 10: ¿Trabajando en calidad de alimentos?: \n\n\t1. Me aburriria \n\n\t2. Me llama la atencion \n\n\t3. Me encantaria \n\nRespuesta: ")
os.system("cls")
while pregunta_10 >= "4":
    print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
    os.system("cls")

contador_respuestas(valor_preguntas(pregunta_10))
pausa()

pregunta_11 = input("pregunta 11: ¿Disfrutas hacer experimentos con distintas sustancias?: \n\n\t1. Poco\n\n\t2. Mas o memnos \n\n\t3. Bastante\n\nRespuesta: ")
os.system("cls")
while pregunta_11 >= "4":
    print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
    os.system("cls")

contador_respuestas(valor_preguntas(pregunta_11))
pausa()

pregunta_12 = input("pregunta 12: ¿Te sientes capacitado para contribuir a un mejor rendimiento en la empresa?: \n\n\t1. Poco\n\n\t2. Mucho\n\n\t3. Bastante\n\nRespuesta: ")
os.system("cls")
while pregunta_12 >= "4":
    print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
    os.system("cls")

contador_respuestas(valor_preguntas(pregunta_12))
pausa()

pregunta_13 = input("pregunta 13: ¿Te interesa aprender como una maquina interactua con un humano?: \n\n\t1. No me veo trabajando con tecnologia \n\n\t2. Me llama la atencion, pero prefiero estar en otra rama de la industria\n\n\t3. Me gustaria dedicarme a eso \n\nRespuesta: ")
os.system("cls")
while pregunta_13 >= "4":
    print("\t\t\tRespuesta incorrecta intenta de nuevo  \n\t\t\t\t.·´¯`(>▂<)´¯`·.\n")
    os.system("cls")

contador_respuestas(valor_preguntas(pregunta_13))
pausa()

total()


lista_preguntas=["pregunta1", "pregunta2", "pregunta_3", "pregunta_4", "pregunta_5", "pregunta_6", "pregunta_7", "pregunta_8"," pregunta_9", "pregunta_10", "pregunta_11", "pregunta_12", "pregunta_13"]

def acum (lista1,lista2):
    lista=[[lista1],[lista2]]
    return lista

acum (contador_respuestas(valor_preguntas(pregunta_1)), lista_preguntas )
