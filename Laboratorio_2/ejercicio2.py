#Papeleria

class Articulo:
    def __init__(self, tipo, precio_compra, especificacion):
        self.tipo = tipo
        self.marca = "HOJITAS" if tipo == "cuaderno" else "RAYAS"
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.30
        self.especificacion = especificacion

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Especificación: {self.especificacion}")
        print(f"Precio Compra: {self.precio_compra}")
        print(f"Precio Venta: {self.precio_venta}")

cuaderno = Articulo("cuaderno", 10.0, "50 hojas")
lapiz = Articulo("lapiz", 1.5, "grafito")
cuaderno.mostrar_informacion()
lapiz.mostrar_informacion()
