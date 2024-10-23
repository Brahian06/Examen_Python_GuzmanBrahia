import json
from empleados import Empleado

class GestionNomina:
    def __init__(self):
        self.empleados = []

    def AgregarEmpleado(self, identificacion, nombre, cargo, salario):
        # Agrega un nuevo empleado al sistema
        empleado = Empleado(identificacion, nombre, cargo, salario)
        self.empleados.append(empleado)
    
    def BuscarEmpleado(self, identificacion):
        # Busca un empleado por su identificación
        for empleado in self.empleados:
            if empleado.identificacion == identificacion:
                return empleado
        return None

    def RegistrarFalta(self, identificacion, fecha):
        # Registra una falta para un empleado específico
        empleado = self.BuscarEmpleado(identificacion)
        if empleado:
            empleado.RegistrarFalta(fecha)
            return f"Falta registrada para {empleado.nombre}"
        else:
            return "Empleado no encontrado"
    
    def RegistrarBono(self, identificacion, fecha, valor, concepto):
        # Registra un bono para un empleado específico
        empleado = self.BuscarEmpleado(identificacion)
        if empleado:
            empleado.RegistrarBono(fecha, valor, concepto)
            return f"Bono registrado para {empleado.nombre}"
        else:
            return "Empleado no encontrado"

    def CalculoNomina(self, identificacion):
        # Calcula la nómina de un empleado específico
        empleado = self.BuscarEmpleado(identificacion)
        if empleado:
            return empleado.CalculoNomina()
        else:
            return "Empleado no encontrado"

    def GuardarDatos(self, archivo):
        # Guarda la información de los empleados en un archivo JSON
        data = [{
            "identificacion": emp.identificacion,
            "nombre": emp.nombre,
            "cargo": emp.cargo,
            "salario": emp.salario,
            "faltas": emp.faltas,
            "bonos": emp.bonos
        } for emp in self.empleados]
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)

    def CargarDatos(self, archivo):
        # Carga la información de los empleados desde un archivo JSON
        with open(archivo, 'r') as f:
            data = json.load(f)
            for emp_data in data:
                empleado = Empleado(
                    emp_data['identificacion'],
                    emp_data['nombre'],
                    emp_data['cargo'],
                    emp_data['salario']
                )
                empleado.faltas = emp_data['faltas']
                empleado.bonos = emp_data['bonos']
                self.empleados.append(empleado)