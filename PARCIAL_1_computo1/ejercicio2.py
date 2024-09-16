# Prgrama para registrar las asistencias de los alumnos

from datetime import datetime

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asistencia = {}
    
    def registrar_asistencia(self, fecha, estado, razon=None):
        self.asistencia[fecha] = {'estado': estado, 'razon': razon}

class Colegio:
    def __init__(self):
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def registrar_asistencia(self, nombre_estudiante, fecha, estado, razon=None):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                estudiante.registrar_asistencia(fecha, estado, razon)
                break
    
    def mostrar_asistencia(self):
        for estudiante in self.estudiantes:
            print(f"Estudiante: {estudiante.nombre}")
            for fecha, info in estudiante.asistencia.items():
                print(f"Fecha: {fecha}, Estado: {info['estado']}, Razón: {info.get('razon', 'N/A')}")

def main():
    colegio = Colegio()
    
    num_estudiantes = int(input("Ingrese el número de estudiantes: "))
    for _ in range(num_estudiantes):
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiante = Estudiante(nombre)
        colegio.agregar_estudiante(estudiante)
    
    while True:
        nombre_estudiante = input("Ingrese el nombre del estudiante para registrar asistencia (o 'fin' para terminar): ")
        if nombre_estudiante.lower() == 'fin':
            break
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        estado = input("Ingrese el estado (Asistencia/Permiso/Inasistencia): ")
        razon = None
        if estado.lower() == "permiso":
            razon = input("Ingrese la razón del permiso: ")
        
        colegio.registrar_asistencia(nombre_estudiante, fecha, estado, razon)
    
    print("Registro de asistencia:")
    colegio.mostrar_asistencia()

if __name__ == "__main__":
    main()
