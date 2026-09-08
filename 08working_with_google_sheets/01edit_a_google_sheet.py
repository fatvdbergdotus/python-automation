import pandas as pd
import gspread
import re

# opening a private google sheet
# the API secret.json is created at console.cloud.google.com
gs = gspread.service_account("secret.json")
spreadsheet = gs.open("pythoncourse")

worksheet1 = spreadsheet.worksheet("Sheet1")

# update a cell
worksheet1.update_acell("A2","xyz")

# update a cell (based on row, column numbers)
worksheet1.update_cell(3,2,"new_value")