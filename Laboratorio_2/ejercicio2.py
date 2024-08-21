class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

# Instancia del objeto llamado AVION
avion = Vehiculo("Avión")
print(f"Este vehículo es un {avion.tipo}.")
