from fpdf import FPDF

def generar_pdf(cuentas, ruta="reporte_banco.pdf"):

    pdf=FPDF()
    pdf.agg_page()

    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,"Sistema de gestión bancaria",ln=True)

    pdf.line=5

    pdf.set_font("Arial", size=11)

    if not cuentas:
        pdf.cell(0,10,"No hay cuentas regustradas.",ln=True)

    for cuenta in cuentas:
        pdf.multi_cell(0,10,cuenta.mostrar_informacion())

    pdf.output(ruta)

    return ruta
