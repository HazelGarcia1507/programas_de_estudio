#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Inicio del programa
#Se incorpora la triple comilla para parrafos

#BIENVENIDA
nombre = input("Como te llamas?")

print(f"""
¡Hola {nombre}!

Vamos a practicar sustantivos, adjetivos y verbos.

¡Diviértete!
""")



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

#Para convertir la letra en respuesta
if sust == "a":
    sust = opciones[0]

elif sust == "b":
    sust = opciones[1]

elif sust == "c":
    sust = opciones[2]


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

    #Para convertir la letra en respuesta
    if sust == "a":
        sust = opciones[0]

    elif sust == "b":
        sust = opciones[1]

    elif sust == "c":
        sust = opciones[2]

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


#Se incorpora la triple comilla para parrafos
#Seccion de ADJETIVOS


sustCorrecto = random.choice(sustantivo)
adjCorrecto = random.choice(adjetivo)
verbCorrecto = random.choice(verbo)

opciones = [sustCorrecto,adjCorrecto,verbCorrecto]
random.shuffle(opciones)

a = opciones[0]
b = opciones[1]
c = opciones[2]

respuesta_correcta = adjCorrecto
intentoAdj = 0

print (f"""Un adjetivo es una palabra que describe
algo como, grande, frio, caliente. Si:
       
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")

adj = input("Cual es un adjetivo? ")

#Para convertir la letra en respuesta
if adj == "a":
    adj = opciones[0]

elif adj == "b":
    adj = opciones[1]

elif adj == "c":
    adj = opciones[2]

while adj != respuesta_correcta and intentoAdj < 2:
    intentoAdj = intentoAdj + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoAdj} intentos
    
 Un adjetivo es una palabra que describe 
 algo como, grande, frio, caliente. Si: 

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)
    adj = input("Cual es un adjetivo? ")

#Para convertir la letra en respuesta
    if adj == "a":
        adj = opciones[0]

    elif adj == "b":
        adj = opciones[1]

    elif adj == "c":
        adj = opciones[2]

if adj == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {adj} es un adjetivo!
    
    Llevas {RC} puntos!
    """)

else:
      intentoAdj = intentoAdj + 1
      print(f"""
      Llevas {intentoAdj} intentos
      
      Lo siento! te quedaste sin intentos!
      """)



#Se incorpora la triple comilla para parrafos
#Seccion de VERBOS

sustCorrecto = random.choice(sustantivo)
adjCorrecto = random.choice(adjetivo)
verbCorrecto = random.choice(verbo)

opciones = [sustCorrecto,adjCorrecto,verbCorrecto]
random.shuffle(opciones)

a = opciones[0]
b = opciones[1]
c = opciones[2]

respuesta_correcta = verbCorrecto
intentoVerb = 0

print (f"""Un verbo es una accion, es algo que alguien 
hace como correr, cantar aprender, escribir. Si:
       
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")

verb = input("Cual es un verbo? ")

#Para convertir la letra en respuesta
if verb == "a":
    verb = opciones[0]

elif verb == "b":
    verb = opciones[1]

elif verb == "c":
    verb = opciones[2]

while verb != respuesta_correcta and intentoVerb < 2:
    intentoVerb = intentoVerb + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoVerb} intentos
    
 Un verbo es una accion, es algo que alguien 
 hace como correr, cantar aprender, escribir. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)

    verb = input("Cual es un verbo? ")


#Para convertir la letra en respuesta
    if verb == "a":
        verb = opciones[0]

    elif verb == "b":
        verb = opciones[1]

    elif verb == "c":
        verb = opciones[2]


if verb == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {verb} es un verbo!
    Llevas {RC} puntos!
    """)
else:
      intentoVerb = intentoVerb + 1
      print(f"""
      Llevas {intentoVerb} intentos
      
      Lo siento! te quedaste sin intentos!
      """)


#Se incorpora la triple comilla para parrafos
#Pregunta extra de juego


mama = "Mama ama mas a Alice"
alice = "Alice ama mas a Mama"
papa = "Papa ama mas a Alice"
bruno = "Bruno ama mas a Alice"


opciones = [mama,alice,papa,bruno]
random.shuffle(opciones)

respuesta_correcta = mama

print(f"""
Hora de la pregunta mas importante! Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
d = {opciones[3]}
""")
mas = input("Quien ama mas a quien?")

#Para convertir la letra en respuesta
if mas == "a":
    mas = opciones[0]

elif mas == "b":
    mas = opciones[1]

elif mas == "c":
    mas = opciones[2]

elif mas == "d":
     mas = opciones [3]


while mas != respuesta_correcta:
     print(f"""
     Incorrecto! Intentalo de nuevo! Si:
     
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
d = {opciones[3]}
    """)

     mas = input("Quien ama mas a quien? ")


    #Para convertir la letra en respuesta
     if mas == "a":
        mas = opciones[0]

     elif mas == "b":
        mas = opciones[1]

     elif mas == "c":
        mas = opciones[2]

     elif mas == "d":
        mas = opciones [3]


RC = RC + 1     
print( f"""
    Correcto! Mama ama mas a Alice!
    Llevas {RC} puntos!
""")



#EVALUACION

msj4 = "Excelente trabajo!! \nTodas tus respuestas fueron correctas! \nFelicidades! Sacaste 100!"
msj3 = "Ya casi lo logras! \nExcelente trabajo! \nSacaste 80!"
msj2 = "Vas mejorando! Muy bien! \nSigue practicando! \nSacaste 60!"
msj1 = "No pasa nada!\nSigamos practicando!"
msj0 = "Tranquila, volveremos a intentarlo!"

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

elif RC == 0:
        print(f"Tuviste {RC} preguntas correctas de 4")
        print(msj0)