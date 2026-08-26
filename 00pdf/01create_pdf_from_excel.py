import pandas as pd
from fpdf import FPDF

df=pd.read_excel('data.xlsx', sheet_name='Sheet 1')

# create a file for each row in the excel file
for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    # print a line for each column in the excel file
    for i in range(5):
        pdf.set_font('Arial', '', 12)
        pdf.cell(w=70, h=15, text=df.columns[i])
        pdf.cell(w=0, h=15, text=row.iloc[i], ln=1)

    pdf.output('01create_pdf_from_excel'+str(index)+'.pdf')




