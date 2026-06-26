######################################
#EJEMPLO PARA USAR FUNCIONES

numero = 5

def duplicar(numero):
    numero = numero * 2
    return(numero)

print (numero)

masa = duplicar(numero)

print (masa)

##################################
#PARA DEVOLVER MAS DE UN VALOR EN LA FUNCION

cantidad = 1

def multiplicar(cantidad):
    mano = cantidad * 2
    pie = cantidad * 2
    brazo = cantidad* 2
    return(mano, pie, brazo)

print (cantidad)

mano,pie,brazo = multiplicar(cantidad)

print (mano)
print (pie)
print(brazo)
print (multiplicar(cantidad))

#####
#Se quitan estas letras porque no se usan, python ya sabe en que posicion estan y que existen esas opciones
    #a = opciones[0]
    #b = opciones[1]
    #c = opciones[2]



####################################         PROGRAMA     ############################

#REPOSITORIOS

import random

sustantivo = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ]
adjetivo = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"]
verbo = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]

#################          SECCION DE VARIABLES
#Para hacer generico el siguiente while y poder imprimirlo se añade:
sust_descripcion = """Un sustantivo es el nombre de algo, 
 puede ser persona, animal o cosa. Si:"""
sust_palabra = "Sustantivo "
adj_descripcion = """Un adjetivo es una palabra que describe
algo como, grande, frio, caliente. Si: """
adj_palabra = "Adjetivo "
verb_descripcion = """Un verbo es una accion, es algo que alguien 
    hace como correr, cantar aprender, escribir. Si: """
verb_palabra = "Verbo "

##################           SECCION DE FUNCIONES

#Opciones random barajadas (ORB) = cada respuesta elegida al azar se muestra en diferente orden
def ORB():
    sustCorrecto = random.choice(sustantivo)
    adjCorrecto = random.choice(adjetivo)
    verbCorrecto = random.choice(verbo)

    opciones = [sustCorrecto,adjCorrecto,verbCorrecto]
    random.shuffle(opciones)

    return(sustCorrecto,adjCorrecto,verbCorrecto,opciones)
#regreso opciones como lista para imprimirla y cada valor por si solo para poder utilizar solo verbCorrecto en la seccion de verbos, etc

sustCorrecto, adjCorrecto, verbCorrecto, opciones = ORB()



#Para convertir letra en respuesta
def letra_respuesta(entrada, opciones): 
     if entrada == "a":
        entrada = opciones[0]

     elif entrada == "b":
        entrada = opciones[1]

     elif entrada == "c":
        entrada = opciones[2]
     return(entrada)


#Para generalizar funcion choose only
def textos_categoria_gramatical ():
    IsustP = "Cual es un sustantivo? "
    IadjP = "Cual es un adjetivo? "
    IverbP = "Cual es un verbo? "
    Qvalid_letter = "Elije una letra que sea valida por favor"
    
    return (IsustP, IadjP, IverbP, Qvalid_letter)

IsustP, IadjP, IverbP, Qvalid_letter = textos_categoria_gramatical()


#Para que el usuario solo pueda dar una letra valida: a,b o c
def choose_only_abc(entrada,gramatica, desc_categoria):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print(Qvalid_letter)
        print (f"""
{desc_categoria}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
   
        entrada = input (gramatica)
    return(entrada)

#NOTA: Se pone gramatica como nombre para saber que ahi puedo utilizar verbos, adjetivos y sustantivos segun corresponda y asi dejar general la funcion. (No se movio en lab 02 y 03 porque solo era una palabra para hacer commit)


####################### INICIA PROGRAMA SECCION DE SUSTANTIVOS #########################

#Lo que ya me dio COABC lo integro en la siguiente linea:
respuesta_correcta = sustCorrecto

#solo contadores
intentoSus = 0
RC = 0


print (f"""
{sust_descripcion}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
# Como se generaliza se cambia sust por entrada
entrada = input(IsustP)


#Para verificar que la entrada sea solo una letra -COABC
entrada = choose_only_abc(entrada, IsustP, sust_descripcion)

#Para convertir la letra en respuesta
entrada = letra_respuesta(entrada,opciones)


while entrada != respuesta_correcta and intentoSus < 2:
    intentoSus = intentoSus + 1

    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoSus} intentos
     
 {sust_descripcion}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)
    entrada = input(IsustP)


    #Para verificar que la entrada sea solo una letra
    entrada = choose_only_abc(entrada,IsustP, sust_descripcion)

    #Para convertir la letra en respuesta
    entrada = letra_respuesta(entrada,opciones)

if entrada == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {entrada} es un {sust_palabra}!
    
    Llevas {RC} punto!
    """)

else:
      intentoSus = intentoSus + 1
      print(f"""
      Llevas {intentoSus} intentos
      
      Lo siento! te quedaste sin intentos!
      """)


###################                   SECCION DE ADJETIVOS              ######################

#Paraa que tenga nuevas palabras:
sustCorrecto, adjCorrecto, verbCorrecto, opciones = ORB()

#En la siguiente linea integro lo que me dio COABC
respuesta_correcta = adjCorrecto

#Contadores
intentoAdj = 0

print (f"""
{adj_descripcion}
       
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")

entrada  = input(IadjP)


#Para verificar que la entrada sea solo una letra
entrada = choose_only_abc(entrada,IadjP, adj_descripcion)


#Para convertir la letra en respuesta
entrada = letra_respuesta(entrada,opciones)


while entrada != respuesta_correcta and intentoAdj < 2:
    intentoAdj = intentoAdj + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoAdj} intentos
    
 {adj_descripcion}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)
    entrada = input(IadjP)


    #Para verificar que la entrada sea solo una letra
    entrada = choose_only_abc(entrada,IadjP, adj_descripcion)
    

    #Para convertir la letra en respuesta
    entrada = letra_respuesta(entrada,opciones)

if entrada == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {entrada} es un {adj_palabra}!
    
    Llevas {RC} puntos!
    """)

else:
      intentoAdj = intentoAdj + 1
      print(f"""
      Llevas {intentoAdj} intentos
      
      Lo siento! te quedaste sin intentos!
      """)


#########################                 SECCION DE VERBOS             ####################

#Paraa que tenga nuevas palabras:
sustCorrecto, adjCorrecto, verbCorrecto, opciones = ORB()

#En la siguiente linea integro lo que me dio COABC
respuesta_correcta = verbCorrecto

#Contadores
intentoVerb = 0


print (f"""
{verb_descripcion}
       
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")

entrada = input(IverbP)


#Para verificar que la entrada sea solo una letra
entrada = choose_only_abc(entrada, IverbP, verb_descripcion)

#Para convertir la letra en respuesta
entrada = letra_respuesta(entrada,opciones)


while entrada != respuesta_correcta and intentoVerb < 2:
    intentoVerb = intentoVerb + 1
    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoVerb} intentos
    
{verb_descripcion}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)

    entrada = input(IverbP)

    #Para verificar que la entrada sea solo una letra
    entrada = choose_only_abc (entrada, IverbP, verb_descripcion)

    #Para convertir la letra en respuesta
    entrada = letra_respuesta(entrada, opciones)


if entrada == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {entrada} es un {verb_palabra}!
    Llevas {RC} puntos!
    """)
else:
      intentoVerb = intentoVerb + 1
      print(f"""
      Llevas {intentoVerb} intentos
      
      Lo siento! te quedaste sin intentos!
      """)

