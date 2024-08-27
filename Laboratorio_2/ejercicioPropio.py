#Libreria

class ProductoLibreria:
    def __init__(self, tipo, titulo, autor_o_editor, precio_compra, categoria):
        self.tipo = tipo  # 'Libro' o 'Revista'
        self.titulo = titulo
        self.autor_o_editor = autor_o_editor
        self.precio_compra = precio_compra
        self.precio_venta = precio_compra * 1.25  # Margen de ganancia del 25%
        self.categoria = categoria  # Género del libro o tipo de revista (semanal/mensual)
    
    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Título: {self.titulo}")
        print(f"Autor/Editor: {self.autor_o_editor}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio Compra: {self.precio_compra}")
        print(f"Precio Venta: {self.precio_venta}")

# Registrando un libro
libro = ProductoLibreria(
    tipo="Libro", 
    titulo="Cien Años de Soledad", 
    autor_o_editor="Gabriel García Márquez", 
    precio_compra=20.0, 
    categoria="Novela"
)

# Registrando una revista
revista = ProductoLibreria(
    tipo="Revista", 
    titulo="National Geographic", 
    autor_o_editor="National Geographic Editors", 
    precio_compra=5.0, 
    categoria="Mensual"
)

# Mostrando la información
libro.mostrar_informacion()
print("\n")
revista.mostrar_informacion()
