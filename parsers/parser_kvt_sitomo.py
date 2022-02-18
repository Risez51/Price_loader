import datetime
import fileWorker
import resultItem
import pandas as pd


class Parser_kvt_sitomo:
    def __init__(self):
        print('КВТ_СИТ - старт обработки.')
        self.file_name = datetime.datetime.today().strftime('%d-%m-%y') + '.xlsx'
        self.url = f'https://kvt.tools/price/storereports/kvt.store-status_{self.file_name}'

    def parse(self):
        data_list = fileWorker.FileReader().get_download_excel_file_numpy(self.url)
        print(f'Парсинг файла поставщика КВТ_СИТ')
        return self.get_result_list(data_list)

    def get_result_list(self, data_list):
        result_list = []
        for item in data_list:
            result_item = resultItem.ResultItem()
            #print(f'артикул:{item[0]}, наименование:{item[2]}, цена:{item[5]}')
            if len(str(item[0])) > 0 and not pd.isnull(item[5]) and item[0] != 'код товара' and isinstance(item[2], str) and len(str(item[2])) > 3:
                result_item.article = item[0]
                result_item.name = item[2]
                result_item.unit = item[3]
                result_item.quantity = item[4] if not pd.isnull(item[4]) else 0
                result_item.purchase_price = float(item[5]) / 1.2
                result_item.selling_price = result_item.purchase_price
                result_item.site_name = result_item.name
            if result_item.article != '':
                result_list.append(result_item.to_dict())
        print(f'Поставщик: КВТ_СИТ, найдено: {len(result_list)} ')
        return result_list

