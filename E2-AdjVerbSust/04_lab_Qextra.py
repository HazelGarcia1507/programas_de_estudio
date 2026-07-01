#opciones/elige
import random

mama = "Mama ama mas a Alice"
alice = "Alice ama mas a Mama"
papa = "Papa ama mas a Alice"

elige = [mama,alice,papa]
random.shuffle(elige)

##################           SECCION DE FUNCIONES





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
def choose_only_abc(entrada,gramatica, desc_categoria,lista):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print(Qvalid_letter)
        print (f"""
{desc_categoria}

a = {lista[0]}
b = {lista[1]}
c = {lista[2]}
""")
   
        entrada = input (gramatica)
    return(entrada)


Q_mas_extra = "Por favor contesta la pregunta mas importante. Si: "
Who_more = "Quien ama mas a quien?"

RC = 0
respuesta_correcta = mama

print(f"""
{Q_mas_extra}

a = {elige[0]}
b = {elige[1]}
c = {elige[2]}
""")
mas = input(Who_more)


#Para verificar que la entrada sea solo una letra
mas = choose_only_abc(mas,Who_more,Q_mas_extra,elige)


#Para convertir la letra en respuesta
mas = letra_respuesta(mas, elige)


while mas != respuesta_correcta:
     print(f"""
     Incorrecto! Intentalo de nuevo! Si:
     
a = {elige[0]}
b = {elige[1]}
c = {elige[2]}
    """)

     mas = input("Quien ama mas a quien? ")


     #Para verificar que la entrada sea solo una letra
     mas = choose_only_abc(mas,Who_more,Q_mas_extra,elige)


     #Para convertir la letra en respuesta
     mas = letra_respuesta(mas, elige)


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