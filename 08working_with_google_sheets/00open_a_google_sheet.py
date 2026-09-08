import pandas as pd
import gspread
import re

# opening a public google sheet
spreadsheet_name = "1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84"
sheet_name1 = "2013"
sheet_name2 = "2014"

url_sheet1 = f"https://docs.google.com/spreadsheets/d/{spreadsheet_name}/gviz/tq?tqx=out:csv&sheet={sheet_name1}"
url_sheet2 = f"https://docs.google.com/spreadsheets/d/{spreadsheet_name}/gviz/tq?tqx=out:csv&sheet={sheet_name2}"
data1 = pd.read_csv(url_sheet1)
data2 = pd.read_csv(url_sheet2)

print(data1)
print(data2)


# opening a private google sheet
# the API secret.json is created at console.cloud.google.com
gs = gspread.service_account("secret.json")
spreadsheet = gs.open("pythoncourse")

worksheet1 = spreadsheet.get_worksheet(0)    # get a work sheet by index
worksheet1 = spreadsheet.worksheet("Sheet1") # get a work sheet by name
data1 = worksheet1.get_values("A1:A5")
print(data1)
data2 = worksheet1.get_values("A1:B1")
print(data2)
data3 = worksheet1.get_values("A1:B5")
print(data3)
data4 = worksheet1.acell("A3").value
print(data4)

worksheet2 = spreadsheet.get_worksheet(1)    # get a work sheet by index
worksheet2 = spreadsheet.worksheet("Sheet2") # get a work sheet by name
data5 = worksheet2.get_all_records()
print(data5)
data6 = worksheet2.col_values(2) # second column
print(data6)
data7 = worksheet2.row_values(3) # third row
print(data7)

# Search for a particular value (one cell)
search_data1 = worksheet1.find("c")
print(search_data1.row, search_data1.col) # returns the row and column number at which the value was found

# Search for a particular value (multiple cells)
search_data2 = worksheet1.findall("c")
for cell in search_data2:
    print(cell.row, cell.col)

# using regular expression
reg = re.compile("\d") # a digit
search_data3 = worksheet1.findall(reg)
for cell in search_data3:
    print(cell.row, cell.col, cell.value)