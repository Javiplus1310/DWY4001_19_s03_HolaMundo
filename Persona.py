

# Vamos a definir una clase. Primero una clase 

class Persona:

    # en python hay un solo "constructor", qe se llama __init__
    # deben recibir un parametro self!!!
    # si se parte con (underscore) _ se debe tratar como si fuera privada
    def __init__(self, nombre, rut):
        self.nombre = nombre
        self.rut = rut
    
    def imprimir(self):
        texto = " ".join(("soy", self.nombre, "mi rut es", self.rut))
        print(texto)


