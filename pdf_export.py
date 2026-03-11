from fpdf import FPDF

def create_pdf(text):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        pdf.multi_cell(0,10,line)

    file_path = "prompt_output.pdf"

    pdf.output(file_path)

    return file_path
