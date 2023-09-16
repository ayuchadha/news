import os

from RPA.Excel.Files import Files


class Excel:
    def __init__(self) -> None:
        self.files = Files()

    def create_excel(self, worksheet_data: dict, filepath: str) -> None:
        """Creates an Excel file with the given news data.
        """
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
            
            self.files.create_workbook()
            self.files.create_worksheet(
                name=f"Sheet1", content=worksheet_data, header=True)
            self.files.save_workbook(filepath)

        finally:
            self.files.open_workbook(filepath)
            if self.files.worksheet_exists(name="Sheet"):
                self.files.remove_worksheet(name="Sheet")
            self.files.save_workbook(filepath)
            pass
