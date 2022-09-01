numero1 = 90 
numero2 = 10   #operador de asigancion 
numero3 = 10
numero4 = 1
numero5 = 9

resta = numero1 - numero2 - numero3
multiplicacion = numero4 * numero5
division = numero1 / numero2
resto = numero1 % numero2 

Calificacion_del_contenido = input ("¿Que te parecio el video del uno al 10?: ") 
Lista_de_calificacion = input ("1 2 3 4 5 6 7 8 9 10, ¿Cual seria tu califiacion del 1 al 10?: ")
Recomendacion_del_contenido = input ("¿En que crees que pudieramos mejorar?: ")

print("*********ENCUESTA***************")
print(f"la resta es: {resta}")  
print(f"la suma es: {numero1 + numero2}")    
print(f"la multiplicacion es: {multiplicacion}")
print(f"la division es: {division}")
print(f"el resto de la division es: {resto}")

print(f"Veo que tu califiacion fue de {Calificacion_del_contenido}")
print(f"Nos podrias decir en que podriamos mejorar? {Lista_de_calificacion}")
print(f"{Recomendacion_del_contenido} muchas gracias por tus recomendaciones:)")