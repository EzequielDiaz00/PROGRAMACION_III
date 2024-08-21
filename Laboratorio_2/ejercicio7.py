class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo

# Instancia del objeto llamado MONSTERSINC
monsters_inc = Pelicula("Monsters Inc.")
print(f"Esta película es {monsters_inc.titulo}.")
