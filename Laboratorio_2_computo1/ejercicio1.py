#Veterinaria

class Perro:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.estado = "ATENDIDO"
        self.tipo = "Perro Grande" if peso >= 10 else "Perro Pequeño"

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Estado: {self.estado}")
        print(f"Tipo: {self.tipo}")

perro = Perro(nombre="Rex", raza="Labrador", edad=5, peso=12)
perro.mostrar_informacion()
