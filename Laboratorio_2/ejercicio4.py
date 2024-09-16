#Almacen de depositos electronicos

class Dispositivo:
    def __init__(self, tipo, modelo, especificacion, precio_compra):
        self.tipo = tipo
        self.marca = "PHR"
        self.modelo = modelo
        self.especificacion = especificacion
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.7
        self.importado = True

    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Especificación: {self.especificacion}")
        print(f"Precio Compra: {self.precio_compra}")
        print(f"Precio Venta: {self.precio_venta}")

celular = Dispositivo("Celular", "PHR-100", "64GB, 4GB RAM", 150)
celular.mostrar_informacion()
