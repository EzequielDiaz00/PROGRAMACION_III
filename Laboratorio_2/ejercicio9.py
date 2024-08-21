class Servicio:
    def __init__(self, tipo):
        self.tipo = tipo

# Instancia del objeto llamado ENERGÍA
energia = Servicio("Energía")
print(f"Este servicio es {energia.tipo}.")
