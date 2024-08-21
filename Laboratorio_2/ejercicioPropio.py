class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
        self.en_movimiento = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El auto {self.marca} {self.modelo} está encendido.")
        else:
            print(f"El auto {self.marca} {self.modelo} ya está encendido.")

    def apagar(self):
        if self.encendido and not self.en_movimiento:
            self.encendido = False
            print(f"El auto {self.marca} {self.modelo} está apagado.")
        elif self.en_movimiento:
            print(f"El auto {self.marca} {self.modelo} no puede apagarse mientras está en movimiento.")
        else:
            print(f"El auto {self.marca} {self.modelo} ya está apagado.")

    def avanzar(self):
        if self.encendido:
            self.en_movimiento = True
            print(f"El auto {self.marca} {self.modelo} está avanzando.")
        else:
            print(f"El auto {self.marca} {self.modelo} no puede avanzar porque está apagado.")

    def retroceder(self):
        if self.encendido:
            self.en_movimiento = True
            print(f"El auto {self.marca} {self.modelo} está retrocediendo.")
        else:
            print(f"El auto {self.marca} {self.modelo} no puede retroceder porque está apagado.")

    def frenar(self):
        if self.en_movimiento:
            self.en_movimiento = False
            print(f"El auto {self.marca} {self.modelo} ha frenado.")
        else:
            print(f"El auto {self.marca} {self.modelo} no está en movimiento para frenar.")

    def estado(self):
        estado_encendido = "encendido" if self.encendido else "apagado"
        estado_movimiento = "en movimiento" if self.en_movimiento else "detenido"
        print(f"El auto {self.marca} {self.modelo} está {estado_encendido} y {estado_movimiento}.")


# Crear una instancia de la clase Auto
mi_auto = Auto("Toyota", "Corolla")

# Llamar a los métodos
mi_auto.encender()
mi_auto.avanzar()
mi_auto.frenar()
mi_auto.retroceder()
mi_auto.frenar()
mi_auto.apagar()
mi_auto.estado()