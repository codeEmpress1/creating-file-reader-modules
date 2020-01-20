# from files.text import ReadTextFile
# from files.csv import ReadCsv
from spreadsheet.csv_spreadsheet import OpenSpreadSheet


def rb(file):
   return file.read_all()


text_file = OpenSpreadSheet('iris.csv')
print(rb(text_file))