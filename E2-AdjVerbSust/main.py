#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Inicio del programa
#Se incorpora la triple comilla para parrafos

#BIENVENIDA
nombre = input("Como te llamas? ")

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


#Para verificar que la entrada sea solo una letra

while adj != "a" and adj != "b" and adj != "c":
     print("Elije una letra que sea valida por favor")
     print (f"""
Un adjetivo es una palabra que describe
algo como, grande, frio, caliente. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
     adj = input("Cual es un adjetivo?")


#Para convertir la letra en respuesta
adj = letra_respuesta(adj)


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


    #Para verificar que la entrada sea solo una letra

    while adj != "a" and adj != "b" and adj != "c":
        print("Elije una letra que sea valida por favor")
        print (f"""
    Un adjetivo es una palabra que describe
    algo como, grande, frio, caliente. Si:

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        adj = input("Cual es un adjetivo?")


    #Para convertir la letra en respuesta
    adj = letra_respuesta(adj)

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


#Para verificar que la entrada sea solo una letra

while verb != "a" and verb != "b" and verb != "c":
     print("Elije una letra que sea valida por favor")
     print (f"""
Un verbo es una accion, es algo que alguien 
hace como correr, cantar aprender, escribir. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
     verb = input("Cual es un verbo?")


#Para convertir la letra en respuesta
verb = letra_respuesta(verb)


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

    #Para verificar que la entrada sea solo una letra

    while verb != "a" and verb != "b" and verb != "c":
        print("Elije una letra que sea valida por favor")
        print (f"""
    Un verbo es una accion, es algo que alguien 
    hace como correr, cantar aprender, escribir. Si:

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        verb = input("Cual es un verbo?")


    #Para convertir la letra en respuesta
    verb = letra_respuesta(verb)


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



#Pregunta extra de juego


mama = "Mama ama mas a Alice"
alice = "Alice ama mas a Mama"
papa = "Papa ama mas a Alice"


opciones = [mama,alice,papa]
random.shuffle(opciones)

respuesta_correcta = mama

print(f"""
Hora de la pregunta mas importante! Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
mas = input("Quien ama mas a quien?")


#Para verificar que la entrada sea solo una letra

while mas != "a" and mas != "b" and mas != "c" and mas != "d":
     print("Elije una letra que sea valida por favor")
     print (f"""
Por favor contesta la pregunta mas importante. Si:

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
     mas = input("Quien ama mas a quien?")


#Para convertir la letra en respuesta
mas = letra_respuesta(mas)


while mas != respuesta_correcta:
     print(f"""
     Incorrecto! Intentalo de nuevo! Si:
     
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)

     mas = input("Quien ama mas a quien? ")


     while mas != "a" and mas != "b" and mas != "c" and mas != "d":
        print("Elije una letra que sea valida por favor")
        print (f"""
    Por favor contesta la pregunta mas importante. Si:

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        mas = input("Quien ama mas a quien?")


     #Para convertir la letra en respuesta
     mas = letra_respuesta(mas)


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

def evaluacion_final ():
     print("Entre a la funcion")
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



evaluacion_final()