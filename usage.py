from files.text import ReadTextFile
# from files.csv import ReadCsv
# from spreadsheet.csv_spreadsheet import OpenSpreadSheet


def rb(file):
   return file.read_last_two()


text_file = ReadTextFile('numbers.txt')
print(rb(text_file), type(rb(text_file)))