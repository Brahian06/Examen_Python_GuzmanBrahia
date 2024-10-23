from gestion import GestionNomina

def mostrar_menu():
    print("\n--- Menu Gestion de Nomina ---")
    print("1. Agregar empleado")
    print("2. Registrar falta")
    print("3. Registrar bono")
    print("4. Calcular nómina")
    print("5. Guardar datos")
    print("6. Cargar datos")
    print("0. Salir")

def main():
    sistema = GestionNomina()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            identificacion = input("Identificacion: ")
            nombre = input("Nombre: ")
            cargo = input("Cargo: ")
            salario = float(input("Salario: "))
            sistema.AgregarEmpleado(identificacion, nombre, cargo, salario)
            print(f"Empleado {nombre} agregado.")

        elif opcion == "2":
            identificacion = input("Identificacion del empleado: ")
            fecha = input("Fecha de la falta (DD-MM-YYYY): ")
            print(sistema.RegistrarFalta(identificacion, fecha))

        elif opcion == "3":
            identificacion = input("Identificación del empleado: ")
            fecha = input("Fecha del bono (DD-MM-YYYY): ")
            valor = float(input("Valor del bono: "))
            concepto = input("Concepto del bono: ")
            print(sistema.RegistrarBono(identificacion, fecha, valor, concepto))

        elif opcion == "4":
            identificacion = input("Identificación del empleado: ")
            nomina = sistema.CalculoNomina(identificacion)
            if isinstance(nomina, dict):
                print(f"\n--- Nomina de {identificacion} ---")
                for clave, valor in nomina.items():
                    print(f"{clave.capitalize()}: {valor}")
            else:
                print(nomina)
        elif opcion == "5":
            archivo = input("Nombre del archivo para guardar (.json): ")
            sistema.GuardarDatos(archivo)
            print("Datos guardados correctamente.")

        elif opcion == "6":
            archivo = input("Nombre del archivo para cargar (.json): ")
            sistema.CargarDatos(archivo)
            print("Datos cargados correctamente.")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()

