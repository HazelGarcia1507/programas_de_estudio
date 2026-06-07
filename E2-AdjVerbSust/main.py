#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Repositorio de Categorias gramaticales

# gramatica = {
#     "sustantivo" = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ],
    
#     "adjetivo" = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"],

#     "verbo" = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]
# }

#Inicio del programa

print ("Un sustantivo es el nombre de algo, puede ser persona, animal")
print ("a = casa"),
print ("b = grande"),
print ("c = correr")

sust = input("Cual es un sustantivo? ")


a = "casa"
b = "grande"
c = "correr"

if sust == a:
    print (f"Correcto! {sust} es un sustantivo!")
else:
    print (f"Error! el sustantivo es casa")




#Repeticion del juego. 
#PENDIENTE CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones



print ("Un adjetivo es una palabra que describe algo como, grande, frio, caliente")
print ("a = perro"),
print ("b = inteligente"),
print ("c = aprender")

adj = input("Cual es un adjetivo? ")


a = "perro"
b = "inteligente"
c = "aprender"

if adj == b:
    print (f"Correcto! {adj} es un adjetivo!")
else:
    print (f"Error! el adjetivo es inteligente")


#Repeticion del juego. 
#PENDIENTE CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones



print ("Un verbo es una accion, es algo que alguien hace como correr, cantar aprender, escribir")
print ("a = medico"),
print ("b = rapido"),
print ("c = construir")

verb = input("Cual es un verbo? ")


a = "medico"
b = "rapido"
c = "construir"

if verb == b:
    print (f"Correcto! {verb} es un verbo!")
else:
    print (f"Error! el verbo es construir")