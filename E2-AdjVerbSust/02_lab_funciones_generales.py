### PARA HACER GENERICA UNA FUNCION  #############

###GUIA###
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



#Para verificar que la entrada sea solo una letra
#COABC


def choose_only_abc(entrada):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print("Elije una letra que sea valida por favor")
        print (f"""
    {sust}

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        entrada = input("Cual es un sustantivo? ")
    return(entrada)





#Para verificar que la entrada sea solo una letra
#COABC

def pregunta_categoria_gramatical ():
    IsustP = input("Cual es un sustantivo? ")
    IadjP = input ("Cual es un adjetivo? ")
    IverbP = input ("Cual es un verbo? ")
    Qvalid_letter = "Elije una letra que sea valida por favor"
    opciones = """
    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}"""
    return (IsustP, IadjP, IverbP, Qvalid_letter, opciones)

IsustP, IadjP, IverbP, Qvalid_letter, opciones = pregunta_categoria_gramatical()

def choose_only_abc(entrada,IsustP):
    while entrada != "a" and entrada != "b" and entrada != "c":
        print("Elije una letra que sea valida por favor")
        print (f"""
    {sust}

    a = {opciones[0]}
    b = {opciones[1]}
    c = {opciones[2]}
    """)
        entrada = IsustP
    return(entrada)