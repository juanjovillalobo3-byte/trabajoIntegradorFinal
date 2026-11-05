from fpdf import FPDF

def generar_pdf(cuentas, ruta="reporte_banco.pdf"):

    pdf=FPDF()
    pdf.add_page()

    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
    pdf.set_top_margin(10)

    pdf.set_font("Arial","B",16)
    pdf.cell(0,10,"Sistema de gestión bancaria",ln=True)

    pdf.set_font("Arial", size=11)

    if not cuentas:
        pdf.cell(0,10,"No hay cuentas regustradas.",ln=True)

    for cuenta in cuentas:
        pdf.multi_cell(0,8,cuenta.mostrar_informacion())
        pdf.ln(5)

    pdf.output(ruta)

    return ruta
