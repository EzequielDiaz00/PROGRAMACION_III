class Dispositivo:
    def __init__(self, tipo):
        self.tipo = tipo

# Instancia del objeto llamado PORTATIL
portatil = Dispositivo("Portátil")
print(f"Este dispositivo es un {portatil.tipo}.")
