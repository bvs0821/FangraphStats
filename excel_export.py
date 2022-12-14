import pandas as pd
import sqlite3
import xlsxwriter
import os
from compile_db import *
cwd = os.getcwd()

#delete all .xlsx files before compiling data
for i in range(365):
    try:
        os.remove(cwd + "/fangraph_{}days.xlsx".format(i))
    except:
        pass

for day in num_days:
    # insert the file path for the Excel wooksheet
    filePath = cwd + '/fangraph_{}days.xlsx'.format(day)

    # create SQLite connection with fangraph SQL database
    conn = sqlite3.connect(cwd + '/fangraph_{}days.db'.format(day))

    writer = pd.ExcelWriter(filePath, engine='xlsxwriter')

    df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)

    for table_name in df['name']:
        sheet_name = table_name
        SQL = "SELECT * FROM " + sheet_name
        dft = pd.read_sql_query(SQL, conn)
        dft.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()

