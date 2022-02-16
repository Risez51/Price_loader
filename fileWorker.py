import pandas as pd
import datetime
from xml.dom import minidom
import urllib.request
import openpyxl


class FileReader:
    def __init__(self, sheet=0):
        self.sheet = sheet

    def get_list_from_excel(self, file_path: str):
        return pd.ExcelFile(file_path).parse(sheet_name=self.sheet, encoding_override='CORRECT_ENCODING').to_numpy()

    def get_list_from_csv(self, file_path: str):
        return pd.read_csv(file_path, sep=";", engine='python', encoding='latin-1').to_numpy()

    def get_xml_file(self, xml_url):
        xml_file = urllib.request.urlopen(xml_url)
        xml_data = xml_file.read()
        dom = minidom.parseString(xml_data)
        dom.normalize()
        return dom

    def get_data_list(self, file_path):
        return self.get_list_from_excel(file_path) if ".xl" in file_path else self.get_list_from_csv(file_path)


class FileWriter:
    def __init__(self, sheet=0, file_name='result'):
        self.sheet = sheet
        self.file_name = file_name

    def to_excel(self, my_data):
        pd.DataFrame(data=my_data).to_excel(self.create_file_name(), index=False)

    def create_file_name(self):
        my_date = datetime.datetime.now()
        return f'./{self.file_name} (от {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'

