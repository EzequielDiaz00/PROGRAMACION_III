# Programa para leer 10 datos característicos de una persona

import tkinter as tk

def mostrar_ventana():
    ventana = tk.Tk()
    ventana.title("Datos Personales")
    ventana.geometry("300x600")

    datos = ["Nombre Completo", "Edad", "Género", "Ocupación", "Teléfono", 
             "Correo Electrónico", "Dirección", "Estado Civil", "Nacionalidad", "Hobbies"]

    for dato in datos:
        tk.Label(ventana, text=dato).pack(pady=5)
        tk.Entry(ventana).pack(pady=5)

    ventana.mainloop()

mostrar_ventana()
