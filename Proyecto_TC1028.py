"""
Proyecto TC1028
"""
import os


print("#################### ANALIZADoR DE CARRERAS ########################")

entrada1 = input(f"pregunta 1: De las siguientes materias ¿Cual es tu favorita?: \n\n\t\t1. Matematicas-Fisica\n\t\t2. Computacion\n\t\t3. Quimica\n\nRespuesta: ")

While = (entrada1 == "1" or "uno"):
respuesta1 = 10
if (entrada1 == "2" or "dos"): 
    respuesta1 = 20
elif (entrada1 == "3" or "tres"):
    respuesta1 = 30 

print(f"El valor de respuesta1 es: {respuesta1}")
    
"""""
entrada2 = input(f"pregunta 2: Para ti ¿Que es la ingenieria?: \n\n\t1. Es el poder crear cosas atarves de la indrustria\n\n\t2. Es el saber como funcionan los aparatos electronicos por dentro\n\n\t3. Es el poder crear soluciones a porblemas atraves de un laboratorio \n\nRespuesta: ")
os.system("cls")
entrada3 = input(f"pregunta 3: ¿Cual crees que sea tu mejor fortaleza?: \n\n\t1. Analisis\n\n\t2. Control bajo estres\n\n\t3. Trabajo en equipo\n\nRespuesta: " )
os.system("cls")
entrada4 = input("pregunta 4: ¿En que area Ingenieril te gustaria desempeñarte?: \n\n\t1. Mecatronica y Robotica\n\n\t2. Tecnologias Computacionales\n\n\t3. Bioingenierias\n\n\t4. Ciencia Aplicadas\n\nRespuesta: ")
os.system("cls")
entrada5 = input(f"pregunta 5: Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas?: \n\n\t- 1\n\n\t- 2\n\n\t- 3 \n\nRespuesta: ")
os.system("cls")
entrada6 = input(f"pregunta 6: ¿En que tipo de industria te ves trabajando en un futuro?: \n\n\t1. Manofuctura y diseño mecanico\n\n\t2. Big TECH\n\n\t3. Aeroespacial\n\n\t4. Alimentaria o relacionados\n\n\t5. Centros de Investigacion\n\n\t6. Aeroespacial o Aeronautica \n\nRespuesta: ")
os.system("cls")
entrada7 = input(f"pregunta 7: ¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso?: \n\n\t1. Analitico\n\n\t2. Creativo\n\n\t3. Ingenioso\n\nRespuesta: ")
os.system("cls")
entrada8 = input(f"pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t1. Visual\n\n\t2. Emocional\n\n\t2. Asociativo\n\nRespuesta: ")
os.system("cls")

#def pregunta_totales(entrada1,entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8):
    

            
if(entrada2 == "1" or "uno"):
    respuesta2 = 10
elif(entrada2 == "2" or "dos"): 
    respuesta2 = 20
elif(entrada2 == "3" or "tres"):
    respuesta2 = 30


if(entrada3 == "1" or "uno"): 
    respuesta3 = 10
elif (entrada3 == "2" or "dos"): 
    respuesta3 = 20
elif (entrada3 == "3"or "tres"):
    respuesta3 = 30
    
if(entrada4 == "1" or "uno"):
    respuesta4 = 10
elif (entrada4 == "2" or "dos"): 
    respuesta4 = 20
elif (entrada4 == "3" or "tres"):
    respuesta4 = 30
elif (entrada4 == "4" or "cuatro"):
    respuesta4 = 40
elif(entrada4 == "5" or "cinco"):
    respuesta4 = 50

if(entrada5 == "1" or "uno"):
    respuesta5 = 10
elif(entrada5 == "2" or "dos"): 
    respuesta5 = 20
elif(entrada5 == "3" or "tres"):
    respuesta5 = 30

if(entrada6 == "1" or "uno"):
    respuesta6 = 10
elif (entrada6 == "2" or "dos"): 
    respuesta6 = 20
elif (entrada6 == "3" or "tres"):
    respuesta6 == 30
elif (entrada6 == "4" or "cuatro"):
    respuesta6 = 40
elif(entrada6 == "5" or "cinco"):
    respuesta6 = 50

if(entrada7 == "1" or "uno"): 
    respuesta7 = 10
elif (entrada7== "2" or "dos"): 
    respuesta7 = 20
elif (entrada7 == "3" or "tres"):
    respuesta7 = 30

if(entrada8 == "1" or "uno"): 
    respuesta8 = 10
elif (entrada8 == "2" or "dos"): 
    respuesta8 = 20
elif (entrada8 == "3" or "tres"):
    respuesta8 = 30
    
puntaje_total = int(respuesta1+respuesta2+respuesta3+respuesta4+respuesta5+respuesta6+respuesta7+respuesta8)


"""""
""" 
 return int (puntaje_total)




rint("######## Resultado del analizador #########")
print(pregunta_totales(entrada1,entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8))

"""

