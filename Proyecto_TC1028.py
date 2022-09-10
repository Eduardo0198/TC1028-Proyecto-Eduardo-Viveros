
#Proyecto TC1028

import os

#Declaración de las variables
Matematicas_Fisica=0
Computacion=0
Quimica=0




print("####################Analizador########################")

entrada1 = input(f"pregunta 1: De las siguientes materias cual es tu favorita: \n\n\t\tMatematicas-Fisica\n\t\tComputación\n\t\tQuimica\n\nRespuesta: ")
os.system("cls")
entrada2 = input(f"pregunta 2: ¿Te gustaria estudiar una ingenieria? ")
os.system("cls")
entrada3 = input(f"pregunta 3: ¿Cual crees que sea tu mejor fortaleza: analisis, liderazgo o productividad?" )
os.system("cls")
entrada4 = input(f"pregunta 4: ¿Que carreras de las siguientes te gustaria estudiar robotica, mecanica o sistemas digitales?")
os.system("cls")
entrada5 = input(f"pregunta 5: Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas? ")
os.system("cls")
entrada6 = input(f"pregunta 6: ¿Cual de las siguientes areas te gusta mas: Programacion, Electronica o construccion-mecanica? ")
os.system("cls")
entrada7 = input(f"pregunta 7: ¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso?")
os.system("cls")
entrada8 = input(f"pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo? ")
os.system("cls")

def pregunta1(entrada1):
    if(entrada1 =='Matematicas-Fisica'):
        Matematicas_Fisica=10
        puntajetotal_pregunta1=10
    elif (entrada1 =='Computacion'): 
        Computacion = 20
        puntajetotal_pregunta1=20
    elif (entrada1 =='Quimica'):
        Quimica = 30
        puntajetotal_pregunta1=30
    
    return puntajetotal_pregunta1

print(pregunta1('Computacion'))

