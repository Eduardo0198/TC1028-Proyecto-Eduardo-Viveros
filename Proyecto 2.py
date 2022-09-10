#Proyecto TC1028

print("############################################")

pregunta1 = ("¿Cual es tu materia favorita? ")
pregunta2 = ("¿Te gustaria estudiar una ingenieria? ")
pregunta3 = ("¿Cual crees que sea tu mejor fortaleza: analisis, liderazgo o productividad? ")
pregunta4 = ("¿Que carreras de las siguientes te gustaria estudiar robotica, mecanica o sistemas digitales? ")
pregunta5 = ("Del 1 al 3 ¿Como es tu desempeño en las materias fisico-matematicas? ")
pregunta6 = ("¿Cual de las siguientes areas te gusta mas: Programacion, Electronica o construccion-mecanica? ")
pregunta7 = ("¿Con cual de las siguientes palabras te identificas: analitico, creativo o ingenioso? ")
pregunta8 = ("¿Eres de un aprendizaje mas visual, emocional o asociativo? ")


respuesta1a = "Matematicas"
respuesta2a = "Si"
respuesta3a = "analisis"
respuesta4a = "robotica"
respuesta5a = "1"
respuesta6a = "Programacion"
respuesta7a = "analitico"
respuesta8a = "visual"

entrada1 = input(f"pregunta 1: {pregunta1}")
entrada2 = input(f"pregunta 2: {pregunta2}")
entrada3 = input(f"pregunta 3: {pregunta3}")
entrada4 = input(f"pregunta 4: {pregunta4}")
entrada5 = input(f"pregunta 5: {pregunta5}")
entrada6 = input(f"pregunta 6: {pregunta6}")
entrada7 = input(f"pregunta 7: {pregunta7}")
entrada8 = input(f"pregunta 8: {pregunta8}")


aciertos1 = False
aciertos2 = False
aciertos3 = False
aciertos4 = False
aciertos5 = False
aciertos6 = False
aciertos7 = False
aciertos8 = False

if(entrada1 == respuesta1a):
    aciertos1 = True
else: 
    aciertos1 = False

if(entrada2 == respuesta2a):
    aciertos2 = True
else: 
    aciertos2 = False

if(entrada3 == respuesta3a):
    aciertos3 = True
else: 
    aciertos3 = False

if(entrada4 == respuesta4a):
    aciertos4 = True
else: 
    aciertos4 = False

if(entrada5 == respuesta5a):
    aciertos5 = True
else: 
    aciertos5 = False

if(entrada6 == respuesta6a):
    aciertos6 = True
else: 
    aciertos6 = False

if(entrada7 == respuesta7a):
    aciertos7 = True
else: 
    aciertos7 = False

if(entrada8 == respuesta8a):
    aciertos8 = True
else: 
    aciertos8 = False

print("\n")
print("#####################################################")



if(aciertos1 == True):
    print("pregunta 1 es correcta")
else:
    print("pregunta 1 es incorrecta")


if(aciertos2 == True):
    print("pregunta 2 es correcta")
else:
    print("pregunta 2 es incorrecta")


if(aciertos3 == True):
    print("pregunta 3 es correcta")
else:
    print("pregunta 3 es incorrecta")


if(aciertos4 == True):
    print("pregunta 4 es correcta")
else:
    print("pregunta 4 es incorrecta")


if(aciertos5 == True):
    print("pregunta 5 es correcta")
else:
    print("pregunta 5 es incorrecta")


if(aciertos6 == True):
    print("pregunta 6 es correcta")
else:
    print("pregunta 6 es incorrecta")


if(aciertos7 == True):
    print("pregunta 7 es correcta")
else:
    print("pregunta 7 es incorrecta")


if(aciertos8 == True):
    print("pregunta 8 es correcta")
else:
    print("pregunta 8 es incorrecta")


