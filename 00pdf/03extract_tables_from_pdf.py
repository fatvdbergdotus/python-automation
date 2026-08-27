import tabula

table  = tabula.read_pdf("weather.pdf", pages=1)

table[0].to_csv("output.csv",index=None)
table[0].to_excel('output.xlsx', index=None)