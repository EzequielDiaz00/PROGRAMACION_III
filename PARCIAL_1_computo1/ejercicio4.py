# Programa para ingresar los datos y mostral el pago de planilla de los trabajadores

class Empleado:
    def __init__(self, nombre, antiguedad):
        self.nombre = nombre
        self.antiguedad = antiguedad

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, antiguedad, salario_base, comisiones):
        super().__init__(nombre, antiguedad)
        self.salario_base = salario_base
        self.comisiones = comisiones
    
    def calcular_salario(self):
        salario = self.salario_base + self.comisiones
        if self.antiguedad >= 5:
            salario += 200  # Bono adicional por años en la empresa
        return salario

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, antiguedad, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre, antiguedad)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        salario = self.horas_trabajadas * self.tarifa_por_hora
        if self.antiguedad >= 5:
            salario += 200  # Bono adicional por años en la empresa
        return salario

def main():
    tipo_empleado = input("Ingrese el tipo de empleado (fijo/por horas): ").lower()
    nombre = input("Ingrese el nombre del empleado: ")
    antiguedad = int(input("Ingrese la antigüedad en años del empleado: "))
    
    if tipo_empleado == "fijo":
        salario_base = float(input("Ingrese el salario base: "))
        comisiones = float(input("Ingrese el monto de las comisiones: "))
        empleado = EmpleadoFijo(nombre, antiguedad, salario_base, comisiones)
    elif tipo_empleado == "por horas":
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
        empleado = EmpleadoPorHoras(nombre, antiguedad, horas_trabajadas, tarifa_por_hora)
    else:
        print("Tipo de empleado no válido.")
        return
    
    print(f"Salario calculado para {nombre}: ${empleado.calcular_salario()}")

if __name__ == "__main__":
    main()
