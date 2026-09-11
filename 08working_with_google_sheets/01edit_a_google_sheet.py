import gspread
import time

# opening a private google sheet
# the API secret.json is created at console.cloud.google.com
gs = gspread.service_account("secret.json")
spreadsheet = gs.open("pythoncourse")

worksheet1 = spreadsheet.worksheet("Sheet1")

# update a cell
worksheet1.update_acell("A2","xyz")

# update a cell (based on row, column numbers)
worksheet1.update_cell(3,2,"new_value")

# update a column
existing_column = worksheet1.get_values("B1:B5")
print(existing_column)
new_column = [float(i[0])*9/5+32 for i in existing_column]
print(new_column)
worksheet1.update("B1:B5", new_column)

# calculate the mean of a column
column_values = worksheet1.get_values("B1:B5")
column_values = [float(i[0]) for i in column_values]
mean_value = sum(column_values) / len(column_values)
print(mean_value)
worksheet1.update("B6", mean_value)

# listening to cell change forever at A2 and copy its value to A10
while True:
    new_value = worksheet1.acell("A2").value
    if new_value != worksheet1.acell("A10").value:
        print("A2 changed to:", new_value)
        worksheet1.update("A10", new_value)
    time.sleep(2)