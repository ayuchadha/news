import os


class DIRECTORIES:
    OUTPUT = os.path.join(os.getcwd(), "output")
    FILEPATH = os.path.join(OUTPUT, "Fresh News.xlsx")
    IMAGE_PATH = os.path.join(OUTPUT, "images")
    ERROR_SCREENSHOT_PATH = os.path.join(OUTPUT, "error.png")
    ARCHIVES_PATH = IMAGE_PATH
