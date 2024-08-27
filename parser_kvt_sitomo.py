import datetime
import fileWorker, resultItem, spotter
import pandas as pd

class Parser_kvt_sitomo:
    def __init__(self):
        print('\nКВТ_СИТ - старт обработки.')
        self.file_name = datetime.datetime.today().strftime('%d-%m-%y') + '.xlsx'
        #self.url = f'https://kvt.tools/price/storereports/kvt.store-status_{self.file_name}'
        self.url = 'http://stock.kvt24.ru/balances/rsk/d73aedb31e887d65d9dd5ca9121700f4.xlsx'

    def parse(self):
        data_list = fileWorker.FileReader().get_download_excel_file_numpy(self.url)
        print(f'Парсинг файла поставщика КВТ_СИТ')
        return self.get_result_list(data_list)

    def get_result_list(self, data_list):
        result_list = []
        for item in data_list:
            result_item = resultItem.ResultItem()
            #print(f'артикул:{item[0]}, наименование:{item[2]}, цена:{item[5]}')
            if len(str(item[1])) > 0:
                result_item.article = item[1]
                result_item.name = item[0]
                result_item.unit = item[7]
                result_item.quantity = spotter.Spotter().get_balance_adjustment_stock(item[4]) if not pd.isnull(item[4]) else 0
                result_item.purchase_price = round(float(item[2].replace(',', '.')) / spotter.Spotter().nds, 2)
                result_item.selling_price = round(result_item.purchase_price, 2)
                result_item.site_name = result_item.name
                result_item.multiplicity = item[3]
                result_item.brand = item[9]
            if result_item.article != '':
                result_list.append(result_item.to_dict())
        print(f'Поставщик: КВТ_СИТ, найдено: {len(result_list)} ')
        return result_list

