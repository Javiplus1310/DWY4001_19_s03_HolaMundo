#!/usr/bin/python3

def funcion_tonta(nombre):
    separador = " "
    mensaje = separador.join(("Oh", "el tonto de" , nombre))
    print (mensaje)

def digito_verificador(rut):
    digito = ""
    contador = 2
    suma = 0
    multiplo = 0
    while rut > 0:
        multiplo = ( rut % 10) * contador
        suma = suma + multiplo
        rut = rut // 10 # division entera
        contador = contador + 1
        if contador == 8 :
            contador = 2
    digito = 11 - (suma % 11)
    if digito == 10:
        digito = 'k'
    if digito == 11 :
        digito = 0
    return str(digito)

mi_rut = 20242724
print("-".join((str(mi_rut), digito_verificador(mi_rut))))

# git add ejemplo_funciones.py
# git commit -m "Agregamos ejemplos funciones"
# git checkout master
# git pull
# git merge dm_ejemplo_funciones
# git push