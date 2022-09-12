
#Proyecto TC1028

import os


print("#################### ANALIZADR ########################")

entrada1 = input(f"pregunta 1: De las siguientes materias ¿Cual es tu favorita?: \n\n\t\t# Matematicas-Fisica\n\t\t# Computacion\n\t\t# Quimica\n\nRespuesta: ")
os.system("cls")
entrada2 = input(f"pregunta 2: ¿Te gustaria estudiar una ingenieria?: \n\n\t# Si\n\n\t# No \n\nRespuesta: ")
os.system("cls")
entrada3 = input(f"pregunta 3: ¿Cual crees que sea tu mejor fortaleza?: \n\n\t# Analisis\n\n\t# Control bajo estres\n\n\t# Liderazgo\n\nRespuesta: " )
os.system("cls")
entrada4 = input("pregunta 4: ¿En que area Ingenieril te gustaria desempeñarte?: \n\n\t# Mecatronica y Robotica\n\n\t# Tecnologias Computacionales\n\n\t# Bioingenierias\n\n\t# Ciencia Aplicadas\n\nRespuesta: ")
os.system("cls")
entrada5 = input(f"pregunta 5: Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas?: \n\n\t# Si\n\n\t# No\n\nRespuesta: ")
os.system("cls")
entrada6 = input(f"pregunta 6: ¿En que tipo de industria te ves trabajando en un futuro?: \n\n\t# Manofuctura y diseño mecanico\n\n\t# Big TECH\n\n\t# Aeroespacial\n\n\t# Alimentaria o relacionados\n\n\t# Centros de Investigacion\n\nRespuesta: ")
os.system("cls")
entrada7 = input(f"pregunta 7: ¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso?: \n\n\t# Analitico\n\n\t# Creativo\n\n\t# Ingenioso\n\nRespuesta: ")
os.system("cls")
entrada8 = input(f"pregunta 8: ¿Eres de un aprendizaje mas visual, emocional o asociativo?: \n\n\t# Visual\n\n\t# Emocional\n\n\t# Asociativo\n\nRespuesta: ")
os.system("cls")

def pregunta_totales(entrada1,entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8):
    
    if(entrada1 == "Matematicas-Fisica" or "matematicas-Fisica"):
        respuesta1 = 10
    elif (entrada1 == "Computacion" or "computacion"): 
        respuesta1 = 20
    elif (entrada1 == "Quimica" or "quimica"):
        respuesta1 = 30
            
    if(entrada2 == "si" or "Si" or "Si"):
        respuesta2 = 10
    elif(entrada2 == "NO" or "no" or "No"): 
        respuesta2 = 20

    if(entrada3 == "Analisis" or "analisis"): 
        respuesta3 = 10
    elif (entrada3 == "Control bajo estres" or "control bajo estres"): 
        respuesta3 = 20
    elif (entrada3 == "Liderzgo"or "liderzgo"):
        respuesta3 = 30
    
    if(entrada4 == "Mecatronica y Robotica" or "mecatronica y robotica" or "Mecatronica y robotica"):
        respuesta4 = 10
    elif (entrada4 == "Tecnologias Computacionales" or "tecnologias computacionales" or "Tecnologias computacionales"): 
        respuesta4 = 20
    elif (entrada4 == "Bioingenierias" or "bioingenierias"):
        respuesta4 = 30
    elif (entrada4 == "Ciencias Aplicadas" or "Ciencia aplicadas" or "ciencias aplicadas"):
        respuesta4 = 40

    if(entrada5 == "si" or "Si" or "Si"):
        respuesta5 = 10
    elif(entrada5 == "NO" or "no" or "No"): 
        respuesta5 = 20

    if(entrada6 == "Manofuctura y diseño mecanico" or "manofuctura y diseño mecanico" or "Manofuctura y Diseño Mecanico"):
        respuesta6 = 10
    elif (entrada6 == "Big TECH" or "big Tech" or "big TECH"): 
        respuesta6 = 20
    elif (entrada6 == "Aeroespacial" or "aeroespacial"):
        respuesta6 = 30
    elif (entrada6 == "Alimentaria o relacionados" or "alimentaria o relacionados"):
        respuesta6 = 40
    elif(entrada6 == "Centros de Investigacion" or "centros de investigacion"):
        respuesta6 = 50

    if(entrada7 == "Analitico" or "analitico"): 
        respuesta7 = 10
    elif (entrada7== "Creativo" or "creativo"): 
        respuesta7 = 20
    elif (entrada7 == "Ingenioso" or "ingenioso"):
        respuesta7 = 30

    if(entrada8 == "Visual" or "visual"): 
        respuesta8 = 10
    elif (entrada8 == "Emocional" or "emocional"): 
        respuesta8 = 20
    elif (entrada8 == "Asociativo" or "asociativo"):
        respuesta8 = 30
    
    puntaje_total = (respuesta1+respuesta2+respuesta3+respuesta4+respuesta5+respuesta6+respuesta7+respuesta8)
    
    return puntaje_total


print(f"Resultado del analizador")
print(pregunta_totales(entrada1,entrada2,entrada3,entrada4,entrada5,entrada6,entrada7,entrada8))
