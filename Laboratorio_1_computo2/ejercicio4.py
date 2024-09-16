# Programa para leer datos básicos de 3 mascotas diferentes

import tkinter as tk

def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("Datos de Mascotas")
    ventana.geometry("300x400")

    for i in range(1, 4):
        tk.Label(ventana, text=f"Mascota {i}:").pack(pady=5)
        tk.Label(ventana, text="Nombre:").pack(pady=2)
        tk.Entry(ventana).pack(pady=2)
        tk.Label(ventana, text="Edad:").pack(pady=2)
        tk.Entry(ventana).pack(pady=2)
        tk.Label(ventana, text="Raza:").pack(pady=2)
        tk.Entry(ventana).pack(pady=2)

    ventana.mainloop()

mostrar_ventana()
