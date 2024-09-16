# Programa para leer número de cédula y nombre completo

import tkinter as tk

def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("Datos de Identificación")
    ventana.geometry("300x200")

    etiqueta_nombre = tk.Label(ventana, text="Nombre Completo:")
    etiqueta_nombre.pack(pady=5)
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack(pady=5)

    etiqueta_cedula = tk.Label(ventana, text="Número de Cédula:")
    etiqueta_cedula.pack(pady=5)
    entrada_cedula = tk.Entry(ventana)
    entrada_cedula.pack(pady=5)

    ventana.mainloop()

mostrar_ventana()
