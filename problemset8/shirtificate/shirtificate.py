from fpdf import FPDF
from PIL import Image
from PIL import ImageOps


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=10, y=50, w=190)
    pdf.set_font("helvetica", style="B", size=40)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", center=True)
    pdf.set_font("helvetica", style="B", size=20)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 175, f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")



if __name__ == "__main__":
    main()

