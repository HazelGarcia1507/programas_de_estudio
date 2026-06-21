numero = 5

def duplicar(numero):
    numero = numero * 2
    return(numero)

print (numero)

masa = duplicar(numero)

print (masa)





#REPOSITORIOS

import random

sustantivo = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ]
adjetivo = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"]
verbo = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]

sustCorrecto = random.choice(sustantivo)
adjCorrecto = random.choice(adjetivo)
verbCorrecto = random.choice(verbo)

opciones = [sustCorrecto,adjCorrecto,verbCorrecto]
random.shuffle(opciones)



#SECCION DE FUNCIONES

#Para convertir letra en respuesta
def letra_respuesta(respuesta): 
     if respuesta == "a":
        respuesta = opciones[0]

     elif respuesta == "b":
        respuesta = opciones[1]

     elif respuesta == "c":
        respuesta = opciones[2]
     return(respuesta)




#Seccion de SUSTANTIVOS

a = opciones[0]
b = opciones[1]
c = opciones[2]


respuesta_correcta = sustCorrecto
intentoSus = 0
RC = 0

print (f"""
Un sustantivo es el nombre de algo, 
puede ser persona, animal o cosa. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
sust = input("Cual es un sustantivo? ")


#Para verificar que la entrada sea solo una letra

while sust != "a" and sust != "b" and sust != "c":
     print("Elije una letra que sea valida por favor")
     print (f"""
Un sustantivo es el nombre de algo, 
puede ser persona, animal o cosa. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
     sust = input("Cual es un sustantivo? ")


#Para convertir la letra en respuesta
sust = letra_respuesta(sust)


while sust != respuesta_correcta and intentoSus < 2:
    intentoSus = intentoSus + 1

    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoSus} intentos
    
 Un sustantivo es el nombre de algo, 
 puede ser persona, animal o cosa. Si: 

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)
    sust = input("Cual es un sustantivo? ")


    #Para verificar que la entrada sea solo una letra

    while sust != "a" and sust != "b" and sust != "c":
        print("Elije una letra que sea valida por favor")
        print (f"""
    Un sustantivo es el nombre de algo, 
    puede ser persona, animal o cosa. Si:

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        sust = input("Cual es un sustantivo?")

        #Para convertir la letra en respuesta
    sust = letra_respuesta(sust)

if sust == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {sust} es un sustantivo!
    
    Llevas {RC} punto!
    """)

else:
      intentoSus = intentoSus + 1
      print(f"""
      Llevas {intentoSus} intentos
      
      Lo siento! te quedaste sin intentos!
      """)


