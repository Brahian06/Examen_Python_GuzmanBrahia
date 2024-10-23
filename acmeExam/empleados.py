class Empleado:
    def __init__(self, identificacion, nombre, cargo, salario):
        self.identificacion = identificacion
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.faltas = []
        self.bonos = []

    def RegistrarFalta(self, fecha):
        # Registra una falta para un empleado
        self.faltas.append(fecha)

    def RegistrarBono(self, fecha, valor, concepto):
        # Registra un bono extra-legal para un empleado
        self.bonos.append({"fecha": fecha, "valor": valor, "concepto": concepto})

    def CalculoNomina(self):
        # Calcula la nómina mensual del empleado
        salariobase = self.salario

        # Descuentos de pension y salud
        descuentopension = salariobase * 0.045
        descuentosalud = salariobase * 0.04

        # Auxilio de transporte si el salario es menor a dos salarios mínimos (2 salarios minimos vigentes = 2.000.000)
        auxiliotransporte = 140606 if self.salario < 2000000 else 0

        # Deduccion por inasistencias
        diaslaborables = 30
        valordia = salariobase / diaslaborables
        deduccionfaltas = len(self.faltas) * valordia

        # Total de bonos
        totalbonos = sum(bono["valor"] for bono in self.bonos)

        # Nomina final
        nomina_final = salariobase - descuentopension - descuentosalud - deduccionfaltas + auxiliotransporte + totalbonos

        return {
            "Salario Base": salariobase,
            "Descuento de Pension": descuentopension,
            "Descuento de Salud": descuentosalud,
            "Deduccion de Faltas": deduccionfaltas,
            "Auxilio de Transporte": auxiliotransporte,
            "Total Bonos": totalbonos,
            "Nomina Final": nomina_final
        }

#