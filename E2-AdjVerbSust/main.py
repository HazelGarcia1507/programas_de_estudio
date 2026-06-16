#Creacion de programa para memorizar que es un Sustantivo, un verbo y un adjetivo

#Repositorio de Categorias gramaticales

# gramatica = {
#     "sustantivo" = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ],
    
#     "adjetivo" = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"],

#     "verbo" = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]
# }



#Inicio del programa
#Se incorpora la triple comilla para parrafos

#BIENVENIDA
nombre = input("Como te llamas?")

print(f"""
¡Hola {nombre}!

Vamos a practicar sustantivos, adjetivos y verbos.

¡Diviértete!
""")

#Seccion de SUSTANTIVOS

a = "casa"
b = "grande"
c = "correr"
intentoSus = 0
RC = 0

print ("""
Un sustantivo es el nombre de algo, 
puede ser persona, animal o cosa. Si:

a = casa
b = grande
c = correr
""")
sust = input("Cual es un sustantivo? ")



while sust !=a and intentoSus < 2:
    intentoSus = intentoSus + 1

    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoSus} intentos
    
    Un sustantivo es el nombre de algo, 
    puede ser persona, animal o cosa. Si: 

    a = casa
    b = grande
    c = correr
    """)
    sust = input("Cual es un sustantivo? ")

if sust == a:
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

a = "perro"
b = "inteligente"
c = "aprender"
intentoAdj = 0

print ("""Un adjetivo es una palabra que describe
algo como, grande, frio, caliente. Si:
       
a = perro
b = inteligente
c = aprender
""")

adj = input("Cual es un adjetivo? ")


while adj !=b and intentoAdj < 2:
    intentoAdj = intentoAdj + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoAdj} intentos
    
    Un adjetivo es una palabra que describe 
    algo como, grande, frio, caliente. Si: 

    a = perro
    b = inteligente
    c = aprender
    """)
    adj = input("Cual es un adjetivo? ")

if adj == b:
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

a = "medico"
b = "rapido"
c = "construir"
intentoVerb = 0

print ("""Un verbo es una accion, es algo que alguien 
hace como correr, cantar aprender, escribir. Si:
       
a = medico
b = rapido
c = construir
""")

verb = input("Cual es un verbo? ")

while verb !=c and intentoVerb < 2:
    intentoVerb = intentoVerb + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoVerb} intentos
    
    Un verbo es una accion, es algo que alguien 
    hace como correr, cantar aprender, escribir. Si:

    a = medico
    b = rapido
    c = construir
    """)

    verb = input("Cual es un verbo? ")

if verb == c:
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

a = "1"
b = "2"

print("""
Hora de la pregunta mas importante! Si:

1 = Mama ama mas a Alice
2 = Alice ama mas a mama
""")
mas = input("Quien ama mas a quien? 1 o 2?")


while mas != a:
     print("""
     Incorrecto! Intentalo de nuevo! Si:
     
1 = Mama ama mas a Alice
2 = Alice ama mas a mama
    """)

     mas = input("Quien ama mas a quien? 1 o 2?")

RC = RC + 1     
print( f"""
Correcto! Mama ama mas a Alice!
Llevas {RC} puntos!
""")



#EVALUACION

msj4 = "Excelente trabajo!! \n Todas tus respuestas fueron correctas! \n Felicidades! Sacaste 100!"
msj3 = "Ya casi lo logras! \n Excelente trabajo! \n Sacaste 80!"
msj2 = "Vas mejorando! Muy bien! \n Sigue practicando! \n Sacaste 60!"
msj1 = "No pasa nada!\n Sigamos practicando!"
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