import resultItem, fileWorker, spotter


class Parser_torg_7:
    def __init__(self):
        print('\nТорг_7_ЧК - старт обработки.')
        self.url_xml_file = 'http://www.inpo.ru/documents/pricelists/pricelist.xml'

    def parse(self):
        file_reader = fileWorker.FileReader()
        print(f'Парсинг файла поставщика Торг_7_ЧК')
        xml_file = file_reader.get_xml_file(self.url_xml_file)
        return self.get_result_list_from_xml(xml_file)

    def get_result_list_from_xml(self, xml_file):
        item_list = xml_file.getElementsByTagName('item')
        result_list = []
        for item in item_list:
            result_item = resultItem.ResultItem()
            for node in item.childNodes:
                if node.nodeType == 1:
                    if node.tagName == 'no':
                        if node.firstChild:
                            result_item.article = node.firstChild.data
                    elif node.tagName == 'title':
                        if node.firstChild:
                            if 'крин' in node.firstChild.data.lower():
                                result_item = None
                                break
                            else:
                                result_item.name = node.firstChild.data
                                result_item.site_name = result_item.name
                    elif node.tagName == 'price':
                        if node.firstChild:
                            result_item.purchase_price = round(float(node.firstChild.data) / spotter.Spotter().nds, 2)
                            result_item.selling_price = round(result_item.purchase_price * 1.35, 2)
                    elif node.tagName == 'unit':
                        if node.firstChild:
                            result_item.unit = node.firstChild.data
                    elif node.tagName == 'free':
                        if node.firstChild:
                            #result_item.quantity = node.firstChild.data
                            result_item.quantity = spotter.Spotter().get_balance_adjustment_stock(node.firstChild.data)
                    elif node.tagName == 'img':
                        if node.firstChild:
                            result_item.photo_url = node.firstChild.data
            if result_item:
                result_list.append(result_item.to_dict())
        print(f'Поставщик: Торг_7_ЧК, найдено: {len(result_list)} ')
        return result_list
