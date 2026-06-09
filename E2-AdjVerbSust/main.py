#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Repositorio de Categorias gramaticales

# gramatica = {
#     "sustantivo" = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ],
    
#     "adjetivo" = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"],

#     "verbo" = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]
# }



#Inicio del programa

a = "casa"
b = "grande"
c = "correr"

print ("Un sustantivo es el nombre de algo, puede ser persona, animal. Si: ")
print ("a = casa"),
print ("b = grande"),
print ("c = correr")
sust = input("Cual es un sustantivo? ")

 
while sust == b or sust == c:
        print (f"Error! intenta de nuevo!")
        print ("Un sustantivo es el nombre de algo, puede ser persona, animal. Si: ")
        print ("a = casa"),
        print ("b = grande"),
        print ("c = correr")
        sust = input("Cual es un sustantivo? ")

        if sust == a:
             print (f"Correcto! {sust} es un sustantivo!")
             break



#Repeticion del juego. 
#PENDIENTE CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones

a = "perro"
b = "inteligente"
c = "aprender"

print ("Un adjetivo es una palabra que describe algo como, grande, frio, caliente")
print ("a = perro"),
print ("b = inteligente"),
print ("c = aprender")

adj = input("Cual es un adjetivo? ")


while adj == a or adj == c:
        print (f"Error! intenta de nuevo!")
        print ("Un adjetivo es una palabra que describe algo como, grande, frio, caliente.  Si: ")
        print ("a = perro"),
        print ("b = inteligente"),
        print ("c = aprender")
        adj = input("Cual es un adjetivo? ")

        if adj == b:
             print (f"Correcto! {adj} es un adjetivo!")
             break




#Repeticion del juego. 
#PENDIENTE CICLO WHILE mientras no de la respuesta correcta y por 3 ocasiones


a = "medico"
b = "rapido"
c = "construir"

print ("Un verbo es una accion, es algo que alguien hace como correr, cantar aprender, escribir")
print ("a = medico"),
print ("b = rapido"),
print ("c = construir")

verb = input("Cual es un verbo? ")

while verb == a or verb == b:
        print (f"Error! intenta de nuevo!")
        print ("Un verbo es una accion, es algo que alguien hace como correr, cantar aprender, escribir.  Si: ")
        print ("a = medico"),
        print ("b = rapido"),
        print ("c = cosntruir")
        verb = input("Cual es un verbo? ")

        if verb == c:
             print (f"Correcto! {verb} es un verbo!")
             break

