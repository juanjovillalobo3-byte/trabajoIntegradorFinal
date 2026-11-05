from banco import Banco
from cuentas import CuentaAhorro, CuentaCorriente
from reportes import generar_pdf

def mostrar_menu():
    print("SISTEMA DE GESTIÓN BANCARIA.")
    print("1- Crear cuenta de ahorro.")
    print("2- Crear cuenta corriente.")
    print("3- Listar cuentas.")
    print("4- Consultar cuentas.")
    print("5- Depositar dinero.")
    print("6- Retirar dinero.")
    print("7- Transferir dinero.")
    print("8- Generar reporte en pdf.")
    print("9- Salir.")

def ejecutar_banco():
    banco = Banco()

    while True:
        mostrar_menu()
        opcion= input("Seleccione una opción: ").strip()

        try:
            if opcion=="1":
                titular=input("Titular: ")
                numero=input("Número de cuenta: ")

                cuenta=CuentaAhorro(titular, numero)
                banco.agregar_cuenta(cuenta)

                print("Cuenta de ahorro creada.")

            elif opcion=="2":
                titular=input("Titular: ")
                numero=input("Número de cuenta: ")

                cuenta=CuentaCorriente(titular,numero,saldo=0)
                banco.agregar_cuenta(cuenta)

                print("Cuenta corriente creada.")

            elif opcion=="3":
                cuentas=banco.listar_cuentas()

                if not cuentas:
                    print("No hay cuentas registradas.")
                else:
                    for cuenta in cuentas:
                        print(cuenta.mostrar_informacion())

            elif opcion=="4":
                numero=input("Número de cuenta: ")
                cuenta=banco.buscar_cuenta(numero)

                if cuenta is None:
                    print("Cuenta no encontrada.")
                else:
                    print(cuenta.mostrar_informacion())

            elif opcion=="5":
                numero=input("Número de cuenta: ")
                cantidad=float(input("Cantidad a depositar: "))
                cuenta=banco.buscar_cuenta(numero)

                if cuenta is None:
                    raise ValueError("Cuenta no encontrada.")

                cuenta.depositar(cantidad)
                print("Deposito hecho correctamente.")

            elif opcion=="6":
                numero=input("Número de cuenta: ")
                cantidad=float(input("Cantidad a retirar: "))
                cuenta=banco.buscar_cuenta(numero)

                if cuenta is None:
                    raise ValueError("Cuenta no encontrada.")

                cuenta.retirar(cantidad)
                print("Retiro hecho correctamente")

            elif opcion=="7":
                origen=input("Número de cuenta de origen: ")
                destino=input("Número de cuenta de detino: ")
                cantidad=float(input("Cantidad a transferir: "))

                banco.transferir(origen,destino,cantidad)
                print("Transferencia realizada con exito.")

            elif opcion=="8":
                ruta=generar_pdf(banco.listar_cuentas())
                print(f"Reporte generado con exito: {ruta}")

            elif opcion=="9":
                print("Saliendo del programa")
                break

            else:
                print("Opción incorrecta.")

        except ValueError as error:
            print(f"Error: {error}")

        except TypeError as error:
            print(f"Error: {error}")

        except (OSError,PermissionError) as error:
            print(f"Error: {error}")

if __name__== "__main__":
    ejecutar_banco()