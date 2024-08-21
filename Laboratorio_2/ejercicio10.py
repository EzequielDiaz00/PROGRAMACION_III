class Empaque:
    def __init__(self, tipo):
        self.tipo = tipo

# Instancia del objeto llamado CAJA
caja = Empaque("Caja")
print(f"Este empaque es una {caja.tipo}.")
