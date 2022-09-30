import pandas as pd
import sqlite3
import xlsxwriter
import os
from fangraphcompiledb import *

for day in num_days:
    # insert the file path for the Excel wooksheet
    filePath = '/Users/brandon/Desktop/fangraphstats/fangraph_data_{}days.xlsx'.format(day)

    # create SQLite connection with fangraph SQL database
    conn = sqlite3.connect('/Users/brandon/Desktop/fangraphstats/fangraph_condensed_{}days.db'.format(day))

    writer = pd.ExcelWriter(filePath, engine='xlsxwriter')

    df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)

    for table_name in df['name']:
        sheet_name = table_name
        SQL = "SELECT * FROM " + sheet_name
        dft = pd.read_sql_query(SQL, conn)
        dft.to_excel(writer, sheet_name=sheet_name, index=False)

    writer.save()

