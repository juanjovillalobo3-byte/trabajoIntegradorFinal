import pytest
from cuentas import Cuenta, CuentaAhorro, CuentaCorriente

def test_cuenta_es_abstracta():
    with pytest.raises(TypeError):
        Cuenta("Ana", "001")

def test_crear_cuenta_ahorro():
    cuenta = CuentaAhorro("Ana", "001", 100)

    assert cuenta.get_titular() == "Ana"
    assert cuenta.get_numero() == "001"
    assert cuenta.get_saldo() == 100


def test_depositar():
    cuenta = CuentaAhorro("Ana", "001")
    cuenta.depositar(500)
    assert cuenta.get_saldo() == 500

def test_deposito_invalido():
    cuenta = CuentaAhorro("Ana", "001")

    with pytest.raises(ValueError):
        cuenta.depositar(-100)

def test_retirar_ahorro():
    cuenta = CuentaAhorro("Ana", "001", 500)
    cuenta.retirar(200)
    assert cuenta.get_saldo() == 300

def test_retiro_ahorro_sin_saldo():
    cuenta = CuentaAhorro("Ana", "001", 100)

    with pytest.raises(ValueError):
        cuenta.retirar(200)

def test_retirar_corriente():
    cuenta = CuentaCorriente("Luis", "002", 1000)
    cuenta.retirar(1500)
    assert cuenta.get_saldo() == -500

def test_retiro_corriente_supera_limite():
    cuenta = CuentaCorriente("Luis", "002", 1000)

    with pytest.raises(ValueError):
        cuenta.retirar(60000)

def test_setters():
    cuenta = CuentaAhorro("Ana", "001")
    cuenta.set_titular("Luis")
    cuenta.set_numero("002")
    cuenta.set_saldo(300)
    assert cuenta.get_titular() == "Luis"
    assert cuenta.get_numero() == "002"
    assert cuenta.get_saldo() == 300
