from cuentas import CuentaAhorro
from reportes import generar_pdf

def test_generar_pdf(tmp_path):
    cuenta = CuentaAhorro("Ana", "001", 1000)
    archivo = tmp_path / "reporte.pdf"
    resultado = generar_pdf([cuenta], str(archivo))
    assert resultado == str(archivo)
    assert archivo.exists()
    assert archivo.stat().st_size > 0

def test_generar_pdf_sin_cuentas(tmp_path):
    archivo = tmp_path / "reporte_vacio.pdf"
    resultado = generar_pdf([], str(archivo))
    assert resultado == str(archivo)
    assert archivo.exists()
