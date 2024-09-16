# Programa que muestre tu nombre completo y edad centrados

import tkinter as tk

def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("Datos Personales")
    ventana.geometry("300x200")

    nombre_completo = "Diego Montoya"
    edad = "28 añitos"

    etiqueta = tk.Label(ventana, text=f"Nombre: {nombre_completo}\nEdad: {edad}", font=("Arial", 14), justify="center")
    etiqueta.pack(expand=True)

    ventana.mainloop()

mostrar_ventana()
