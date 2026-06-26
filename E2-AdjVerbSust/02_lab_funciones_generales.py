### PARA HACER GENERICA UNA FUNCION  #############
#Seccion de ADJETIVOS

import random

sustantivo = ["casa", "perro", "medico", "computadora", "mexico", "amor", "guitarra", "parque", "felicidad", "estudiante" ]
adjetivo = ["grande", "inteligente", "rapido", "azul", "antiguo", "amable", "roto", "brillante", "frio", "divertido"]
verbo = ["correr", "cantar", "aprender", "escribir", "dormir", "construir", "pensar", "cocinar", "escuchar", "viajar" ]


### SECCION DE VARIABLES
adj_descripcion = """Un adjetivo es una palabra que describe
algo como, grande, frio, caliente. Si: """
adj_palabra = "Adjetivo"


### SECCION DE FUNCIONES###

#Para funcion que da un orden aleatorio de respuestas barajadas
def ORB():
    sustCorrecto = random.choice(sustantivo)
    adjCorrecto = random.choice(adjetivo)
    verbCorrecto = random.choice(verbo)

    opciones = [sustCorrecto,adjCorrecto,verbCorrecto]
    random.shuffle(opciones)
    return (sustCorrecto,adjCorrecto,verbCorrecto, opciones)

sustCorrecto,adjCorrecto,verbCorrecto, opciones = ORB()



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
def pregunta_categoria_gramatical ():
    IsustP = "Cual es un sustantivo? "
    IadjP = "Cual es un adjetivo? "
    IverbP = "Cual es un verbo? "
    Qvalid_letter = "Elije una letra que sea valida por favor"
    
    return (IsustP, IadjP, IverbP, Qvalid_letter)

IsustP, IadjP, IverbP, Qvalid_letter = pregunta_categoria_gramatical()


#Para que el usuario solo pueda dar una letra valida: a,b o c
def choose_only_abc(entrada,IadjP):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print(Qvalid_letter)
        print (f"""
{adj_descripcion}

a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")
   
        entrada = input (IadjP)
    return(entrada)

#En la siguiente linea integro lo que me dio COABC
respuesta_correcta = adjCorrecto

#Contadores
intentoAdj = 0
RC = 0

print (f"""
{adj_descripcion}
       
a = {opciones[0]}
b = {opciones[1]}
c = {opciones[2]}
""")

entrada  = input(IadjP)


#Para verificar que la entrada sea solo una letra
entrada = choose_only_abc(entrada,IadjP)


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
    entrada = choose_only_abc(entrada,IadjP)
    

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
