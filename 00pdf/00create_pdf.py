from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# w=width, h=height, x=x-coordinate
pdf.image('tiger.jpeg', w=80, h=50, x=500)

pdf.set_font('Arial', 'B', 24)
# w=0 means full width, ln=1 means move to next line after this cell
pdf.cell(w=0, h=15, txt="Malayan Tiger", align='C', ln=1)

pdf.set_font('Arial', 'B', 14)
pdf.cell(w=0, h=15, txt="Description", ln=1)

malay_tiger_txt = '''
The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. 
This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. 
As of April 2014, the population was estimated at 80-120 mature individuals, with a continuing downward trend.
'''
pdf.set_font('Arial', '', 12)
pdf.multi_cell(w=0, h=15, txt=malay_tiger_txt, ln=1)

pdf.cell(w=70, h=15, txt="Kingdom")
pdf.cell(w=0, h=15, txt="Animalia", ln=1)

pdf.cell(w=70, h=15, txt="Phylum")
pdf.cell(w=0, h=15, txt="Chordata", ln=1)

pdf.cell(w=70, h=15, txt="Class")
pdf.cell(w=0, h=15, txt="Mammalia", ln=1)

pdf.output('00create_pdf.pdf')
