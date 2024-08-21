class Libro:
    def __init__(self, genero):
        self.genero = genero

# Instancia del objeto llamado NOVELA
novela = Libro("Novela")
print(f"Este libro es una {novela.genero}.")
