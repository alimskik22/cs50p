from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 28)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    shirt_width = 180
    x = (210 - shirt_width) / 2  
    pdf.image("shirtificate.png", x=x, y=60, w=shirt_width)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
