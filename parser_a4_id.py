import resultItem, fileWorker, spotter


class Parser_a4_id:
    def __init__(self):
        print('\nА4_ИД - старт обработки.')
        self.url_xml_file = 'http://aet-auto.ru/files/storage/price.xml'

    def parse(self):
        file_reader = fileWorker.FileReader()
        xml_file = file_reader.get_xml_file(self.url_xml_file)
        return self.get_result_list_from_xml(xml_file)

    def get_result_list_from_xml(self, xml_file):
        item_list = xml_file.getElementsByTagName('offer')
        result_list = []
        for item in item_list:
            support_code = item.getAttribute('id')
            result_item = resultItem.ResultItem()
            for node in item.childNodes:
                if node.nodeType == 1:
                    if node.tagName == 'vendorCode':
                        if node.firstChild:
                            result_item.article = node.firstChild.data + ' ' + support_code
                    elif node.tagName == 'name':
                        if node.firstChild:

                            if 'AE&T' not in node.firstChild.data:
                                #print(f'{node.firstChild.data} === aet в название НЕТ')
                                result_item = None
                                break
                            else:
                                #print(f'{node.firstChild.data} === aet в название ЕСТЬ')
                                result_item.name = node.firstChild.data
                                result_item.site_name = result_item.name
                    elif node.tagName == 'price-dealer':
                        if node.firstChild:
                            result_item.purchase_price = float(node.firstChild.data) / spotter.Spotter().nds
                            if result_item.purchase_price == '' or result_item.purchase_price is None:
                                result_item.purchase_price = 0
                            result_item.selling_price = float(result_item.purchase_price) * 1.4
                    elif node.tagName == 'gk_balance_available':
                        if node.firstChild:
                            if node.firstChild.data == '[[+tv_gk_balance_available]]':
                                result_item.quantity = 0
                            else:
                                result_item.quantity = node.firstChild.data
                                #result_item.quantity = spotter.Spotter().get_balance_adjustment_stock(node.firstChild.data)
            if result_item and result_item.article == 'TC-adapter 4886':
                print(result_item)
            if result_item:
                result_list.append(result_item.to_dict())

        return result_list
