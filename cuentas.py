from abc import ABC, abstractmethod
#Clase abstarcta
class cuenta (ABC):
    def __init__(self, titular, numero, saldo=0):
        self.__titular= titular
        self.__numero= numero
        self.__saldo= saldo

    def titular (self):
        return self.__titular

    def numero (self):
        return self.__numero

    def saldo (self):
        return self.__saldo

    def saldo (self, nuevo_saldo):
        if nuevo_saldo<0:
            raise ValueError("El saldo no puede ser negativo.")
        self.__saldo=nuevo_saldo

    def depositar(self, cantidad):
        if cantidad<=0:
            raise ValueError("El depósito debe ser mayor a cero.")

        self.__saldo+=cantidad

    def retirar(self, cantidad):
        pass

    def mostrar_informacion(self):
        return( 
            f"Titular: {self.__titular}"
            f"Número: {self.__numero}"
            f"Saldo: {self.__saldo}")

class cuentaAhorro(cuenta):
    def retirar (self,cantidad):
        if cantidad<=0:
            raise ValueError("El valor debe ser mayor que cero.")

        if cantidad>self.__saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo=self.saldo-cantidad

class cuentaCorriente(cuenta):
    def __inint__(self,titular,numero,saldo,limite=50000):
        super().__init__(titular,numero,saldo)
        self.__limite=limite

    def limite(self):
        return self.__limite

    def retirar(self,cantidad):
        if cantidad<=0:
            raise ValueError("El retiro debe ser mayor que cero.")
        if cantidad>self.saldo+self.__limite:
            raise ValueError("Se superó el límite.")

        self.saldo=self.saldo-cantidad