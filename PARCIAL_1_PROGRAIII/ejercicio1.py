class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

class Venta:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
    
    def calcular_total(self):
        return sum(producto.precio_unitario * cantidad for producto, cantidad in self.productos)
    
    def mostrar_factura(self):
        print("Factura:")
        for producto, cantidad in self.productos:
            print(f"{producto.nombre}: {cantidad} x ${producto.precio_unitario} = ${producto.precio_unitario * cantidad}")
        total = self.calcular_total()
        print(f"Total: ${total}")
        return total

class Proveedor:
    def __init__(self):
        self.inventario = {}
    
    def recibir_producto(self, nombre_producto, cantidad, precio_sugerido):
        self.inventario[nombre_producto] = {
            'cantidad': cantidad,
            'precio_sugerido': precio_sugerido
        }

def main():
    venta = Venta()
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto vendido (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        cantidad = int(input("Ingrese la cantidad vendida: "))
        
        producto = Producto(nombre_producto, precio_unitario)
        venta.agregar_producto(producto, cantidad)
    
    total = venta.mostrar_factura()
    
    # Manejo del pago
    monto_recibido = float(input("Ingrese el monto recibido del cliente: "))
    
    if monto_recibido < total:
        print(f"El monto recibido es insuficiente. Se requiere ${total - monto_recibido} más.")
    else:
        cambio = monto_recibido - total
        print(f"El cambio a devolver al cliente es: ${cambio:.2f}")
    
    proveedor = Proveedor()
    
    while True:
        nombre_producto = input("Ingrese el nombre del producto recibido del proveedor (o 'fin' para terminar): ")
        if nombre_producto.lower() == 'fin':
            break
        cantidad = int(input("Ingrese la cantidad recibida: "))
        precio_sugerido = float(input("Ingrese el precio sugerido del producto: "))
        
        proveedor.recibir_producto(nombre_producto, cantidad, precio_sugerido)
    
    print("Inventario de proveedores:")
    for nombre_producto, detalles in proveedor.inventario.items():
        print(f"{nombre_producto}: Cantidad {detalles['cantidad']}, Precio sugerido ${detalles['precio_sugerido']}")

if __name__ == "__main__":
    main()
