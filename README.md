# TC1028_Proyecto_Eduardo_Viveros
# ANALIZADOR DE INGENIERIAS 

Vivimos en una realidad donde el mundo parece que todo el tiempo esta cambiando, un gran ejemplo de esto es la pandemia, este evento que vivimos en conjunto como  sociedad nos dejó marcados, una de sus muchas consecuencias es que muchos jóvenes tuvimos que vivir nuestra preparatoria en una computadora, como sabrán el hecho de estar en una sesión de zoom a estar de forma presencial en un salón es un cambio abismal y para muchos jóvenes la transición de una a otra no es nada sencilla haciendo que nos sentiamos perdidos a la hora de elegir una carrera.  

Al ser un proceso muy complicado el elegir una carrera, existen distintos medios para revisar que tipo es la de adecuada para ti. La ingenieria es un campo muy extenso, esta tiene muchas ramas a las que te puedes dedicar, desde dedicarte a la industria y a los procesos manofactura, dedicarte al desarrollo de nuevas tecnologias, crear protesis roboticas para las personas con alguna discapacidad, crear estrategias para que una empresa crezca y ejemplos se sobrarian. Por eso es que me di a la tartea de crear un analizador de ingenierias, el cual te indicara cual es la ideal para ti.

El proyecto tiene un algoritmo de progrmacion el cual consiste en brindar una serie de preguntas para que el usuario las responda, cada pregunta esta diseñada para poder ir identificanddo a lo largo del test a que tipo de area en la ingenieria es mejor para ti . 
El programa corre en Phython 3. Una vez que sepas a que area es la mejor para ti, te indicara 3 posibles opciones de ingenieria a la que te puedieras dedicar, cabe aclarar que si respondes una respuesta que no sea correcta este te retornara, hasta que metas una respuesta valida.


Pseudocodigo

Inicio

##Funcion valida mi respuesta (Entrada)
  
  Entrada (Escribe("Ingresa el numero de la opcion que deseas: "))
    
  Mientras (entrada >=4  o  entrada == 0):
    
   imprime("Respuesta incorrecta intenta de nuevo ·¯`(>▂<)´¯·.")
      
  Entrada (Escribe("Ingresa el numero de la opcion que deseas: "))
    
  Retorna Entrada
  
  Fin-funcion

##Funcion valor res (respuesta):
  
  Inicio

  si respuesta = 1:
       
   res = 10
  
  si tambien respuesta = 2:
       
   res = 20
  
  si tambien respuesta = 3:
       
   res = 30
  
  sino: 
      
   res= 0
    
  retorna res
  
  Fin-funcion 


##Funcion contador de respuestas(res):

  Inicio 
  
  lista = []
  
  listas.agrega (res)       
  
  retorna lista

  Fin-funcion

##Funcion total (lista):

   Inicio 
   
   total = 0
   
   Para i en lista:
      
   total = total + i
  
  imprime("(⌐■_■) El total de puntos es: ", total)
   
   Retorna total
   
   Fin-funcion


##Funcion indicador de carrera (total):
    
  Inicio

  Si total <= 130:
       
  imprime ("""Tengo tres opciones para ti:
                     1. Ingeniero Mecanico
                     2. Ingeniero Aeronautica
                     3. Ingeniero Mecatronico""")
    
   si tambien total <= 260:
         
  imprime ("""Tengo tres opciones para ti:
                       1. Ingeniero en Robotica y Sistemas
                       2. Ingeniero en Sistemas Computacionales 
                       3. Ingeniero en Electronica""")
    
  si tambien total <= 390:
   imprime ("""Tengo tres opciones para ti:
                       1. Ingeniero Quimico
                       2. Ingeniero en Biotecnologia
                       3. Ingeniero en Alimentos""")
                     
  retorna total
  
  Fin-funcion

##Funcion pausa ()
  
  inicio
  Imprime ("Presiona enter para poder continuar") 
  os.system(cls)

  Fin-funcion


Preguntas_diccionario {
                          1 : Pregunta1
                          2 : Pregunta2
                          3 : Pregunta3
}

<!-- ------------------------- ##Cuerpo del codigo ------------------------- -->

Imprime (Preguntas_diccionario[1])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

Imprime (Preguntas_diccionario[2])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

Imprime (Preguntas_diccionario[3])
contador_respuestas(valor_res(valida_respuesta()))
pausa()

Fin


Nota: Ocupe la libreria os.system en la funcion de pausa.
      Esta libreria se ocupa para borrar la pantalla por
      completo para dejar la terminal limpia para el sig
      uiente impresion. Descubri la funcion por que tenia
      la necesidad de que mi programa se limpiara cada 
      que cada vez que se respondiera un pregunta, pude 
      encontrar esta libreria en un video de youtube, y 
      esta libreria tambien es parte de phython.

      URL: https://youtu.be/tJxcKyFMTGo