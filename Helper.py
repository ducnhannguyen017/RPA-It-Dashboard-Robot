from string import ascii_uppercase
from RPA.Excel.Files import Files


class BuildExcelHelper:

    def __init__(self, values):
        self.excel = Files()
        self.values = values

    def run(self):
        self.excel.create_workbook("output/Agencies.xlsx")
        self.excel.rename_worksheet("Sheet", "Agencies")
        row_number = 1
        for agency in self.values:
            for num, val in enumerate(self.values[row_number-1].values()):
                self.excel.set_cell_value(
                    row_number, ascii_uppercase[num], val, "Agencies")
            row_number += 1
        self.excel.save_workbook()
