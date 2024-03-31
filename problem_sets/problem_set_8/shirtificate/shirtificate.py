from fpdf import FPDF


class Shirt(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 50)
        self.cell(0, 60, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')


    def put_name_on_shirt(self, name):
        self.set_font('helvetica', 'B', 30)
        self.set_text_color(255, 255, 255)
        self.text(x=55, y=148.5, txt=f'{name} took CS50')


    def save_the_file(self):
        self.output('shirtificate.pdf')


def main():
    create_pdf(input('Your name: '))


def create_pdf(name):
    pdf = Shirt()
    pdf.add_page()
    pdf.image("shirtificate.png", w=pdf.epw)
    pdf.put_name_on_shirt(name)
    pdf.save_the_file()


if __name__ == '__main__':
    main()
