       
"############ PROYECTO TC1028 #############"

#Biblioteca
import os

"""
=================== funciones auxiliares  ==============================
"""

def valida_respuesta():
    """
   (uso de funciones y ciclos)
   recibe: numero
   La funcion comienza con un input donde tienes que ingresar el numero 
   de opcion que quieras, este input se va a encargar de convertir el
   string en un entero, para asi poder crear una condicion con ciclo 
   while, siendo que mientras que metas un numero mayor o igual a 4, el
   ciclo te va regresar hasta que cumplas con la condicion.
    """
    numero = int(input("\nIngresa el numero de la opcion que deseas: "))
    
    while (numero >=4  or numero == 0):
      print("\n\nRespuesta incorrecta intenta de nuevo \n\t.·¯`(>▂<)´¯·.")
      
      numero = int(input("\nIngresa el numero de la opcion que deseas: "))
    
    return numero

def valor_res (respuesta):
    """
    (uso de funciones, condicionales y operadores boleanos)
    recibe: respuesta
    la funcion ocupa el entero del 1 al 3 que recibe como parametro,
    para poder asignarle un valor a dicho numero con los condicionales, 
    siendo 1 igual 10, 2 igual a 20, 3 igual a 30, para al final solo 
    retornar el valor de la respuesta.
    """
    if respuesta == 1:
       res = 10
    
    elif respuesta == 2:
       res = 20
    
    elif respuesta == 3:
       res = 30
    
    else: 
       res= 0
    
    return res


def contador_respuestas(res):
   """
   (uso de funciones y listas)
   recibe: res
   La funcion recibe los valores de las respuestas, estos mismo se van ir
   acumulando dentro de una lista, cabe aclarar que esta lista se va ir 
   actualizando conforme el usuario vaya llenando el analizador, esto lo 
   logre al declarar una lista sin elementos arriba del main, por lo tanto
   lo que nos va retornar esta funcion, es una lista de 13 datos que son
   producto de las 13 preguntas.
   """
   lista.append(res)       

   return lista


def total (lista):
   """
   (uso de funciones, listas y ciclos)
   recibe: Lista
   La funcion recibe una lista de 13 elementos, con ciclo for me encargue
   que este fuera sumando toda la lista dato por dato, logre esto al 
   usar un acumulador con el nombre "total" y usando "i" como una variable 
   que fuera recorriendo la lista. Esta funcion se mandara a llamar la final
   del main, es por eso que ocupo el print, para que el usuario pueda 
   visualizar su resultado.
   """
   total=0
   for i in lista:
      total=total+i
    
   print("\t (⌐■_■) El total de puntos es: \t", total)
   
   return total



def indicador_de_carrera (total):
    """
    (uso de funciones y condicionales)
    recibe: total
    La funcion ocupa el total para poder definir a que ingenieria vas,
    recordemos que este total es la suma del valor de tus 13 preguntas, por
    lo tanto comparamos los posibles valores que te pudieron salir, como
    son 13 preguntas y las posibles respuestas son 1 = 10, 2 = 20 y 3 = 30, 
    siendo que las respuestas 1 son directamente relacionadas con ingenieria 
    mecanica y mecatronica, las respuestas 2 son directamenente relacionadas con 
    el area de sistemas y las respuestas 3 son directamente relacionadas con el
    area de bioingenierias.
    """
    if total <= 130:
       print ("""\t\nTengo tres opciones para ti:\n\n\t
                     1. Ingeniero Mecanico\n\n\t 
                     2. Ingeniero Aeronautica\n\n\t
                     3. Ingeniero Mecatronico\n""")
    
    elif total <= 260:
         print ("""\t\nTengo tres opciones para ti:\n\n\t
                       1. Ingeniero en Robotica y Sitesmas\n\n\t
                       2. Ingeniero en Sistemas Computacionales \n\n\t
                       3. Ingeniero en Electronica\n""")
    
    elif total <= 390:
         print ("""\t\nTengo tres opciones para ti:\n\n\t
                       1. Ingeniero Quimico,\n\n\t
                       2. Ingeniero en Biotecnologia,\n\n\t
                       3. Ingeniero en Alimentos\n""")
                     
    return total

def pausa ():
    """
    (uso de funciones)
    Sin parametro.
    La funcion introduce un input para tener una pequeña pausa entre pregunta.
    """
    reset = input("\nPresiona enter para poder continuar(☞ﾟヮﾟ)☞")
    
    os.system("cls")

#Diccionario de preguntas
   
"""
(uso de diccionarios o lista anidada)
Esta orginalmente seria una lista anidada llena de mis preguntas que se irian
imprimiendo a lo largo del analizador, incluso considere la idea de hacer una 
lista normal llena de variables, estas variables serian el string de la pregunta,
pero analizando mejor el problema conclui que un diccionario arreglaria mejor
el problema, la forma algo peculiar de imprimir es por que tuve que acomodar 
los prints en base al formato. Los datos dentro del diccionario se mandan a 
llamar en el cuerpo cuerpo del progrmama.
"""

preguntas_dicc = {
       
        1 :"""Pregunta 1:\n ¿Cual es tu materia favorita?:\n\t
              1. Matematicas-Fisica\n\t
              2. Computacion\n\t
              3. Quimica\n""",
        2 :"""Pregunta 2:\nPara ti ¿Que es la ingenieria?:\n\t
              1. Es el poder crear cosas atarves de 
                 la indrustria\n\t
              2. Es el saber como funcionan los aparatos 
                 por dentro\n\t
              3. Es el poder crear soluciones a porblemas 
                 atraves de un laboratorio \n\n""",
        3 :"""Pregunta 3:\n¿Cual es tu mayor fortaleza?:\n\t
              1. Analisis\n\t
              2. Control bajo estres\n\t
              3. Trabajo en equipo\n\n""",
        4 :"""Pregunta 4:\n¿En que area te gustaria trabajr?:\n\t
              1. Mecatronica y Robotica\n\t
              2. Tecnologias Computacionales\n\t
              3. Bioingenierias\n\n""",
        5 :"""Pregunta 5:\n¿cual es tu nivel en mate y fisica:\n\t
              1. Incipiente\n\t
              2. Solido\n\t
              3. Destacado\n\n""",
        6 :"""Pregunta 6:\n¿En que empresa te ves trabajando?:\n\t
              1. Manufactura y diseño mecanico\n\t
              2. Big TECH\n\t
              3. Industria Aliemtaria\n\n""",
        7 :"""Pregunta 7:\n¿Que palabra te identifica mas?:\n\t
              1. Analitico\n\t
              2. Creativo\n\t
              3. Ingenioso\n\n""",
        8 :"""Pregunta 8:\nEres de una aprendizaje mas......:\n\t
              1. Visual\n\t
              2. Practico\n\t
              3. Asociativo\n\n""",
        9 :"""Pregunta 9:\n¿Sientes gusto por la electronica?:\n\t
              1. Es algo que me encanta\n\t
              2. Me llama la atencion\n\t
              3. No me interesa \n\n""",
        10 :"""Pregunta 10:\nTrabajar con alimentos, me.....\n\t
               1. Me aburriria\n\t
               2. Me llama la atencion\n\t
               3. Me encantaria \n\n""",
        11 :"""Pregunta 11:\n¿Disfrutas hacer experimentos?:\n\t
               1. Poco\n\t
               2. Mas o memnos\n\t
               3. Bastante\n\n""",
        12 :"""Pregunta 12:\n¿Te sie?:\n\t
               1. Poco\n\t
               2. Mucho\n\t
               3. Bastante\n\n""",
        13 :"""Pregunta 13:\n¿?:\n\t
               1. No me veo trabajando con tecnologia\n\t
               2. Me llama la atencion pero no estoy seguro\n\t
               3. Me gustaria dedicarme a eso \n\n"""
}
"""
============================ Variables ===========================
"""

lista = []

"""
====================== Cuerpo del programa =======================
"""

print("\n\t\t        BIENVENIDO AL")  
n = ("\n\t(*￣3￣) analizador de ingenierias ( ͡° ͜ʖ ͡°)")
print(n.upper())
print("""
  \n       DONDE TE ORIENTAREMOS A DECIDIR CUAL ES LA MEJOR 
   CARRERA PARA TI POR FAVOR CONTESTA LAS SIGUIENTES PREGUNTAS \n\n""")


print(preguntas_dicc[1])
contador_respuestas(valor_res(valida_respuesta()))
pausa()


print(preguntas_dicc[2])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[3])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[4])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[5])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[6])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[7])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[8])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[9])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[10])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[11])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[12])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

print(preguntas_dicc[13])
contador_respuestas(valor_res(valida_respuesta()))
pausa()


indicador_de_carrera(total(lista))

