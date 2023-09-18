import os

from RPA.Excel.Files import Files


class Excel:
    def __init__(self) -> None:
        self.files = Files()

    def create_excel(self, worksheet_data: dict, filepath: str) -> None:
        """Creates an Excel file with the given news data.
        """
        
        if os.path.exists(filepath):
            os.remove(filepath)
        
        self.files.create_workbook()
        self.files.create_worksheet(
            name=f"Sheet1", content=worksheet_data, header=True)
        
        if self.files.worksheet_exists(name="Sheet"):
            self.files.remove_worksheet(name="Sheet")
        self.files.save_workbook(filepath)
        