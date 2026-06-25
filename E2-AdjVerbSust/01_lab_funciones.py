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


#SECCION DE FUNCIONES

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

#Para hacer generico el siguiente while y poder imprimirlo se añade:
sust = """Un sustantivo es el nombre de algo, 
 puede ser persona, animal o cosa. Si:"""
sustP = "Cual es un sustantivo? "
sus = "Sustantivo "

#Para convertir letra en respuesta
def letra_respuesta(entrada, opciones): 
     if entrada == "a":
        entrada = opciones[0]

     elif entrada == "b":
        entrada = opciones[1]

     elif entrada == "c":
        entrada = opciones[2]
     return(entrada)



def pregunta_categoria_gramatical ():
    IsustP = "Cual es un sustantivo? "
    IadjP = "Cual es un adjetivo? "
    IverbP = "Cual es un verbo? "
    Qvalid_letter = "Elije una letra que sea valida por favor"
    
    return (IsustP, IadjP, IverbP, Qvalid_letter)

IsustP, IadjP, IverbP, Qvalid_letter = pregunta_categoria_gramatical()



def choose_only_abc(entrada,IsustP):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print(Qvalid_letter)
        print (f"""
{sust}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
   
        entrada = input (IsustP)
    return(entrada)




#Seccion de SUSTANTIVOS

#Para tener guardada las opciones que ya me dio ORB uso:
sustCorrecto, adjCorrecto, verbCorrecto, opciones = ORB()

#solo contadores
intentoSus = 0
RC = 0



print (f"""
{sust}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
# Como se generaliza se cambia sust por entrada
entrada = input("Cual es un sustantivo? ")


#Para verificar que la entrada sea solo una letra -COABC
entrada = choose_only_abc(entrada, IsustP)

#Para convertir la letra en respuesta
entrada = letra_respuesta(entrada,opciones)

#Lo que ya me dio COABC lo integro en la siguiente linea:
respuesta_correcta = sustCorrecto



while entrada != respuesta_correcta and intentoSus < 2:
    intentoSus = intentoSus + 1

    print(f"""
    Error! Intenta de nuevo!
    
    Llevas {intentoSus} intentos
    
    {sust}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
    """)
    entrada = input(sustP)


    #Para verificar que la entrada sea solo una letra
    entrada = choose_only_abc(entrada,IsustP)

    #Para convertir la letra en respuesta
    entrada = letra_respuesta(entrada,opciones)

if entrada == respuesta_correcta:
    RC = RC + 1
    print(f"""
    Correcto! {entrada} es un {sus}!
    
    Llevas {RC} punto!
    """)

else:
      intentoSus = intentoSus + 1
      print(f"""
      Llevas {intentoSus} intentos
      
      Lo siento! te quedaste sin intentos!
      """)


