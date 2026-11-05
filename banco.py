from cuentas import Cuenta

class Banco:
    def __init__(self):
        self.__cuentas=[]

    def agregar_cuenta(self,cuenta):
        if self.buscar_cuenta(cuenta.get_numero()) is not None:
            raise ValueError("Ya existe una cuenta con ese número.")

        self.__cuentas.append(cuenta)

    def buscar_cuenta(self,numero):
        for cuenta in self.__cuentas:
            if cuenta.get_numero()==numero:
                return cuenta

        return None

    def listar_cuentas(self):
        return self.__cuentas.copy()

    def transferir(self,origen,destino,cantidad):
        cuenta_origen=self.buscar_cuenta(origen)
        cuenta_destino=self.buscar_cuenta(destino)

        if cuenta_origen is None:
            raise ValueError("No existe la cuenta de origen.")
        if cuenta_destino is None:
            raise ValueError("No existe la cuenta de destino.")

        cuenta_origen.retirar(cantidad)
        cuenta_destino.depositar(cantidad)