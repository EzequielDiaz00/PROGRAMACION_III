#Consesionaria de autos

class Auto:
    def __init__(self, marca, modelo, año, tipo, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo
        self.ruedas = 4
        self.pasajeros = 5
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.4

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Tipo: {self.tipo}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.pasajeros}")
        print(f"Precio Compra: {self.precio_compra}")
        print(f"Precio Venta: {self.precio_venta}")

auto = Auto("Toyota", "Corolla", 2023, "Nacional", 20000)
auto.mostrar_informacion()
