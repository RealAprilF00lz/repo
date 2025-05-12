from fpdf import FPDF,Align

name=input('Your name: ')
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=30)
pdf.cell(text="CS50 Shirtificate",center=True)
pdf.image(name='https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png',x=Align.C,y=35)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(255,255,255)
pdf.cell(text=f"{name} took CS50",center=True,h=230)
pdf.output("shirtificate.pdf")
