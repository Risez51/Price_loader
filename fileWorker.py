import os
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
        try:
            xml_file = urllib.request.urlopen(xml_url)
            xml_data = xml_file.read()
            dom = minidom.parseString(xml_data)
            dom.normalize()
            print(f'Файл по ссылке:{xml_url} - получен.')
            return dom
        except ConnectionError:
            print(f'Ссылка: {xml_url} - НЕДОСТУПНА')

    def get_local_xml_file(self, xml_url):
        with open(xml_url, 'rb') as f:
            xml_data = f.read()
            dom = minidom.parseString(xml_data)
            dom.normalize()
            print(f'Файл по ссылке:{xml_url} - получен.')
        return dom


    def get_download_excel_file_numpy(self, file_url):
        try:
            my_file = urllib.request.urlopen(file_url)
            file_data = my_file.read()
            df_numpy = pd.ExcelFile(file_data).parse(sheet_name=self.sheet, encoding_override='CORRECT_ENCODING').to_numpy()
            print(f'Файл по ссылке:{file_url} - получен.')
            return df_numpy
        except ConnectionError:
            print(f'Ссылка: {file_url} - НЕДОСТУПНА')

    def get_data_list(self, file_path):
        return self.get_list_from_excel(file_path) if ".xl" in file_path else self.get_list_from_csv(file_path)


class FileWriter:
    def __init__(self, sheet=0, supplier_name='result'):
        self.sheet = sheet
        self.supplier_name = supplier_name

    def to_excel(self, my_data):
        file_name = self.create_file_name()
        pd.DataFrame(data=my_data).to_excel(file_name, index=False)
        file_chk_name = file_name.replace('xlsx', 'chk')
        os.rename(file_name, file_chk_name)
        print(f'Поставщик {self.supplier_name}: обработан, создан результирующий файл: {file_name}')


    # def create_file_name(self):
    #     my_date = datetime.datetime.now()
    #     folder_name = my_date.strftime('%d.%m.%y')
    #     return f'C:\\Users\\OperTech\\Desktop\\выгрузка\\{folder_name}\\{self.supplier_name} (от' \
    #            f' {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'

    def create_file_name(self):
        my_date = datetime.datetime.now()
        return f'{self.supplier_name} (от' \
               f' {my_date.day}-{my_date.month}-{my_date.year}) (в {my_date.hour}-{my_date.minute}).xlsx'

    def check_folder(self):
        my_date = datetime.datetime.today().strftime('%d.%m.%y')
        if not os.path.exists(f'C:\\Users\\OperTech\\Desktop\\выгрузка\\{my_date}'):
            print('Папка создана')
            os.makedirs(f'C:\\Users\\OperTech\\Desktop\\выгрузка\\{my_date}')
        else:
            print('Папка уже существует')
