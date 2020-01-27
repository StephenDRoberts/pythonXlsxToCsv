import pandas as pd
import os

from openpyxl import load_workbook

path = "./"  # The folder containing the spreadsheets
sheets = os.listdir(path)
wanted = {'.xlsx'}


for sheet in sheets:
	ext = os.path.splitext(sheet)[1]
        if ext in wanted:
			base = os.path.splitext(sheet)[0]
			csv_name = '%s.csv' % base

			read_file = pd.read_excel (sheet).to_csv (csv_name, index = None, header=True)

			print('Created CSV: %s' % csv_name)