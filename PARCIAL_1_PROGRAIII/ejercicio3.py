class Habitacion:
    def __init__(self, tipo, precio_noche):
        self.tipo = tipo
        self.precio_noche = precio_noche

class Reserva:
    def __init__(self, habitacion, noches):
        self.habitacion = habitacion
        self.noches = noches
        self.servicios_extra = {}
    
    def agregar_servicio_extra(self, servicio, costo):
        self.servicios_extra[servicio] = costo
    
    def calcular_total(self):
        total_habitacion = self.habitacion.precio_noche * self.noches
        total_servicios = sum(self.servicios_extra.values())
        return total_habitacion + total_servicios
    
    def mostrar_factura(self):
        print(f"Habitación: {self.habitacion.tipo}")
        print(f"Precio por noche: ${self.habitacion.precio_noche}")
        print(f"Noches: {self.noches}")
        print(f"Subtotal habitación: ${self.habitacion.precio_noche * self.noches}")
        for servicio, costo in self.servicios_extra.items():
            print(f"{servicio}: ${costo}")
        print(f"Total: ${self.calcular_total()}")

def main():
    tipo_habitacion = input("Ingrese el tipo de habitación (ejm., Suite): ")
    precio_noche = float(input("Ingrese el precio por noche: "))
    noches = int(input("Ingrese el número de noches: "))
    
    habitacion = Habitacion(tipo_habitacion, precio_noche)
    reserva = Reserva(habitacion, noches)
    
    while True:
        servicio = input("Ingrese un servicio extra solicitado (o 'fin' para terminar): ")
        if servicio.lower() == 'fin':
            break
        costo = float(input(f"Ingrese el costo del servicio {servicio}: "))
        reserva.agregar_servicio_extra(servicio, costo)
    
    print("Factura:")
    reserva.mostrar_factura()

if __name__ == "__main__":
    main()
