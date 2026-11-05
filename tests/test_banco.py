import pytest
from banco import Banco
from cuentas import CuentaAhorro

def test_agregar_cuenta():
    banco = Banco()
    cuenta = CuentaAhorro("Ana", "001")
    banco.agregar_cuenta(cuenta)
    assert len(banco.listar_cuentas()) == 1

def test_buscar_cuenta():
    banco = Banco()
    cuenta = CuentaAhorro("Ana", "001")
    banco.agregar_cuenta(cuenta)
    assert banco.buscar_cuenta("001") == cuenta

def test_buscar_cuenta_inexistente():
    banco = Banco()
    assert banco.buscar_cuenta("999") is None

def test_cuenta_duplicada():
    banco = Banco()
    banco.agregar_cuenta(CuentaAhorro("Ana", "001"))

    with pytest.raises(ValueError):
        banco.agregar_cuenta(CuentaAhorro("Luis", "001"))

def test_transferencia():
    banco = Banco()
    origen = CuentaAhorro("Ana", "001", 1000)
    destino = CuentaAhorro("Luis", "002", 500)
    banco.agregar_cuenta(origen)
    banco.agregar_cuenta(destino)
    banco.transferir("001", "002", 300)
    assert origen.get_saldo() == 700
    assert destino.get_saldo() == 800

def test_transferencia_cuenta_inexistente():
    banco = Banco()
    banco.agregar_cuenta(CuentaAhorro("Ana", "001", 1000))

    with pytest.raises(ValueError):
        banco.transferir("001", "999", 100)
