class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

# Instancia del objeto llamado CARRO
carro = Vehiculo("Carro")
print(f"Este vehículo es un {carro.tipo}.")
