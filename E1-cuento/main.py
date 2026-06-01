#Creacion de programa para compresion lectora e identificacion de categoria gramatical verbos, adjetivos y sustantivos

#Seccion de verbo
print ("Un verbo es una accion que alguien hace: correr, caminar, hablar, nadar, comer")
verb1 = input ('Dame un verbo que te guste hacer en la escuela: ').lower()
verb2 = input ('Dame un verbo que te de miedo hacer: ').lower()
verb3 = input ('Dame un verbo que acabas de hacer: ').lower()

#Seccion de Sustantivos
print ("Un sustantivo es el nombre de una persona, cosa, animal o lugar: coche, casa, arbol, gato, perro")
sust1 = input ('Dame un sustantivo que sea de una cosa: ').lower()
sust2 = input ('Dame un sustantivo que sea tu lugar favorito: ').lower()
sust3 = input ('Dame un sustantivo que sea un animal: ').lower()
sust4 = input ('Dame un sustantivo que sea un lugar a donde quieras viajar: ').lower()

#Seccion de adjetivos
print ("Un adjetivo es una palabra que describe como es algo: Grande, suave, bueno, feliz, triste")
adj1 = input ('Dame un adjetivo que te cause asco: ').lower()
adj2 = input ('Dame un adjetivo que te cause risa: ').lower()
adj3 = input ('Dame un adjetivo que te cause emocion: ').lower()

#Seccion de la historia
print(f"Habia una vez un@ {sust1} que vivia en un@ {sust2}")
print(f"Un dia decidio {verb1} porque se sentia muy {adj1}")
print(f"Mientras intentaba {verb1} encontro un@ {sust3} muy {adj2}@")
#Pendiente en adj2 resolver el genero, por lo pronto se deja un @ como solucion
print(f"Entonces los dos comenzaron a {verb2} juntos")
print(f"Al final llegaron a un@ {sust4} donde todo parecia  increiblemente {adj3}")
print(f"Y desde ese dia nunca dejaron de {verb3}")



#PENDIENTES:
#Jugar muchas veces y encontrar frases raras.
#Corregir la historia para que tenga sentido con más combinaciones.
#Agrupar el programa en partes (modulos)
#Agregar una segunda y tercera historia (y como elegirlos al azar).
#Agregar preguntas de comprensión.
#Agregar puntuación.
#Agregar while.
#Validaciones.
#HTML.