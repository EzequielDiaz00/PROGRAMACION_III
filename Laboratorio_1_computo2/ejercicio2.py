# Programa para leer una clave secreta sin mostrar caracteres

import tkinter as tk

def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("Clave Secreta")
    ventana.geometry("300x150")

    etiqueta = tk.Label(ventana, text="Introduce tu clave secreta:", font=("Arial", 12))
    etiqueta.pack(pady=10)

    clave_secreta = tk.Entry(ventana, show="*")
    clave_secreta.pack(pady=10)

    ventana.mainloop()

mostrar_ventana()
