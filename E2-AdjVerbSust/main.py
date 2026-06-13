#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Repositorio de Categorias gramaticales

# gramatica = {
#     "sustantivo" = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ],
    
#     "adjetivo" = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"],

#     "verbo" = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]
# }



#Inicio del programa
#Se añadio los 3 intentos del ciclo while

#Seccion de SUSTANTIVOS

a = "casa"
b = "grande"
c = "correr"
intentoSus = 0
RC = 0

print ("Un sustantivo es el nombre de algo, puede ser persona, animal o cosa. Si: ")
print ("a = casa"),
print ("b = grande"),
print ("c = correr")
sust = input("Cual es un sustantivo? ")



while sust !=a and intentoSus < 2:
    print(f"Error! Intenta de nuevo!")
    intentoSus = intentoSus + 1
    print("")
    print(f"Llevas {intentoSus} intentos")
    print ("")
    print("Un sustantivo es el nombre de algo, puede ser persona, animal o cosa. Si: ")
    print("a = casa")
    print("b = grande")
    print("c = correr")
    sust = input("Cual es un sustantivo? ")

if sust == a:
    print("")
    print(f"Correcto! {sust} es un sustantivo!")
    print("")
    RC = RC + 1
    print(f"Llevas {RC} punto!")
    print("")

else:
      intentoSus = intentoSus + 1
      print("")
      print(f"Llevas {intentoSus} intentos")
      print("")
      print("Lo siento! te quedaste sin intentos!")
      print("")


#LISTO CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones
#Seccion de ADJETIVOS

a = "perro"
b = "inteligente"
c = "aprender"
intentoAdj = 0

print ("Un adjetivo es una palabra que describe algo como, grande, frio, caliente")
print ("a = perro"),
print ("b = inteligente"),
print ("c = aprender")

adj = input("Cual es un adjetivo? ")


while adj !=b and intentoAdj < 2:
    print(f"Error! Intenta de nuevo!")
    intentoAdj = intentoAdj + 1
    print("")
    print(f"Llevas {intentoAdj} intentos")
    print ("")
    print ("Un adjetivo es una palabra que describe algo como, grande, frio, caliente")
    print ("a = perro"),
    print ("b = inteligente"),
    print ("c = aprender")
    adj = input("Cual es un adjetivo? ")

if adj == b:
    print("")
    print(f"Correcto! {adj} es un adjetivo!")
    print("")
    RC = RC + 1
    print (f"Llevas {RC} puntos!")
    print ("")

else:
      intentoAdj = intentoAdj + 1
      print("")
      print(f"Llevas {intentoAdj} intentos")
      print("")
      print("Lo siento! te quedaste sin intentos!")
      print("")



#LISTO CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones
#Seccion de VERBOS

a = "medico"
b = "rapido"
c = "construir"
intentoVerb = 0

print ("Un verbo es una accion, es algo que alguien hace como correr, cantar aprender, escribir")
print ("a = medico"),
print ("b = rapido"),
print ("c = construir")

verb = input("Cual es un verbo? ")

while verb !=c and intentoVerb < 2:
    print(f"Error! Intenta de nuevo!")
    intentoVerb = intentoVerb + 1
    print("")
    print(f"Llevas {intentoVerb} intentos")
    print ("")
    print ("Un verbo es una accion, es algo que alguien hace como correr, cantar aprender, escribir")
    print ("a = medico"),
    print ("b = rapido"),
    print ("c = construir")
    verb = input("Cual es un verbo? ")

if verb == c:
    print("")
    print(f"Correcto! {verb} es un verbo!")
    print("")
    RC = RC + 1
    print (f"Llevas {RC} puntos!")
    print("")
else:
      intentoVerb = intentoVerb + 1
      print("")
      print(f"Llevas {intentoVerb} intentos")
      print("")
      print("Lo siento! te quedaste sin intentos!")
      print("")


#Pregunta extra de juego

a = "1"
b = "2"

print("Hora de la pregunta mas importante! Si:")
print("")
print(" 1 = Mama ama mas a Alice")
print(" 2 = Alice ama mas mama")
print("")
mas = input("Quien ama mas a quien? 1 o 2?")


while mas != a:
     print("")
     print("incorrecto! Intentalo de nuevo! Si: ")
     print("")
     print(" 1 = Mama ama mas a Alice")
     print (" 2 = Alice ama mas mama")
     mas = input("Quien ama mas a quien? 1 o 2?")
     
print("Correcto! Mama ama mas a Alice!")
RC = RC + 1
print (f"Llevas {RC} puntos!")
print("")



#EVALUACION
a = "1"
b = "2"
puntoExtra = 1

print ("Si la opcion 1 es Calificacion ")
print ("Y la opcion 2 son Respuestas correctas")
print ("")
total = input("Como quieres tu resultado? 1 o 2?")
print ("")

while total != a and total != b :
    print("Intenta con otra opcion")
    print("")
    print ("Si la opcion 1 es Calificacion ")
    print ("Y la opcion 2 son Respuestas correctas")
    print("")
    total = input("Como quieres tu resultado? 1 o 2?")
    print("")
    
    
if total == a:
    calif = 10 - intentoSus - intentoAdj - intentoVerb + puntoExtra
    print ("Felicidades!")
    print (f"Tu calificacion final es: {calif}")

elif total == b:
    
    msj4 = "Excelente trabajo!! Todas tus respuestas fueron correctas! Felicidades!"
    msj3 = "Ya casi lo logras! Excelente trabajo!"
    msj2 = "Vas mejorando! Muy bien! Sigue practicando!"
    msj1 = "No pasa nada! Sigamos practicando!"

    if RC == 4:
         print (f"Tuviste {RC} preguntas correctas de 4!")
         print (msj4)

    elif RC == 3:
         print (f"Tuviste {RC} preguntas correctas de 4!")
         print (msj3)

    elif RC == 2:
         print (f"Tuviste {RC} preguntas correctas de 4!")
         print (msj2)   

    elif RC == 1:
         print (f"Tuviste {RC} preguntas correctas de 4!")
         print (msj1)
