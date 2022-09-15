#Inicio

print()
print("Bienvenido a un juego de prueba")
print()

Jugador = input("Ingrese su nombre: ")
print()

print("Bienvenido" , Jugador)
print("Este programa calcula tu conocimiento sobre Destiny 2 .")
print()

#comienzo
Intentos = 1
print("Tienes 1 intento")

#Preguntas

Pregunta1 = "Destiny 2 fue lanzado en el año..."
Pregunta2 = "Caide-6 Murio a manos de..."
Pregunta3 = "Bastion de sombras es..."

#Opciones

opciones1 = ["2017,2018,2019,2020"]
opciones2 = ["Mara Sov, Ulden Sov, Bungie,As de picas"]
opciones3 = ["Jardin de la Salvacion, Xenofago, Buen DLC, Una mierda"]

#Respuestas

Respuesta1 = "2017"
Respuesta2 = "Ulden Sov"
Respuesta3 = "Una mierda"

#Entrada

print("Opciones", opciones1)
entrada1 = input("Pregunta: " + Pregunta1)
print()

print("Opciones", opciones2)
entrada2 = input("Pregunta: " + Pregunta2)
print()

print("Opciones", opciones3)
entrada3 = input("Pregunta: " + Pregunta3)
print()

#Salida
if Pregunta1 == Respuesta1:
    print("Correcto")
    if Pregunta2 == Respuesta2:
        print("Correcto")
        if Pregunta3 == Respuesta3:
            print("Correcta")
            
else:
    print("Incorrecta")

#Fin
print()
print("Fin del juego, gracias por interactuar.")
print("Att: Suka")