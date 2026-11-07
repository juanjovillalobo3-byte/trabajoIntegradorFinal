from abc import ABC, abstractmethod

class Cuenta (ABC):
    def __init__(self, titular, numero, saldo=0):
        self.__titular= titular
        self.__numero= numero
        self.__saldo= saldo


    def get_titular (self):
        return self.__titular

    def set_titular(self, nuevo_titular):
        if not isinstance(nuevo_titular, str) or not nuevo_titular.strip():
            raise ValueError("El titular no puede estar vacío.")

        self.__titular = nuevo_titular.strip()

    def get_numero (self):
        return self.__numero

    def set_numero(self, nuevo_numero):
        if not isinstance(nuevo_numero, str) or not nuevo_numero.strip():
            raise ValueError("El número no puede estar vacío.")

        self.__numero = nuevo_numero.strip()

    def get_saldo (self):
        return self.__saldo

    def set_saldo(self, nuevo_saldo):
        if (not isinstance(nuevo_saldo, (int, float))
                or isinstance(nuevo_saldo, bool)
                or nuevo_saldo < 0):
            raise ValueError("El saldo debe ser un número no negativo.")

        self.__saldo = nuevo_saldo

    def _actualizar_saldo(self,nuevo_saldo):
        self.__saldo=nuevo_saldo

    def depositar(self, cantidad):
        if cantidad<=0:
            raise ValueError("El depósito debe ser mayor a cero.")

        self.__saldo+=cantidad

    @abstractmethod
    def retirar(self, cantidad):
        pass

    def mostrar_informacion(self):
        return( 
            f"Titular: {self.__titular}\n"
            f"Número: {self.__numero}\n"
            f"Saldo: ${self.__saldo}")

class CuentaAhorro(Cuenta):
    def retirar (self,cantidad):
        if cantidad<=0:
            raise ValueError("El valor debe ser mayor que cero.")

        if cantidad>self.get_saldo():
            raise ValueError("Saldo insuficiente.")

        self.set_saldo(self.get_saldo()-cantidad)

class CuentaCorriente(Cuenta):
    def __init__(self,titular,numero,saldo,limite=50000):
        super().__init__(titular,numero,saldo)
        self.__limite=limite

    def get_limite(self):
        return self.__limite

    def retirar(self,cantidad):
        if cantidad<=0:
            raise ValueError("El retiro debe ser mayor que cero.")
        if cantidad>self.get_saldo()+self.__limite:
            raise ValueError("Se superó el límite.")

        nuevo_saldo=self.get_saldo()-cantidad
        self._actualizar_saldo(nuevo_saldo)