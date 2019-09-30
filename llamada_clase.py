
# del archivo Persona.py importa la clase Persona
from Persona import Persona

# Ahora "el main", que esta fuera de la clase.

perrin = Persona("Faker Plus", "20242724-3")
perrin.imprimir()

# en python los atrbutos son publicos, por lo tanto se pueden modficar libremente
perrin.rut = "20123456-7"
perrin.imprimir()

# las clases parten con Mayusculas y usan camel! mientras las funciones usan 
# minusculas y se conectan con underscore
# ej clase(mal) almnno_duoc -> (bien) AumnoDuoc
# ej funcion (mal) imprimirDetalles -> (bien) imprimir_detalles

# Ej: crear na persona leyendo desde la consola:
nombre = input("Ingrese un nombre: ")
rut = input("Ingrese el rut: ")
personaIngresada = Persona(nombre, rut)
personaIngresada.imprimir()