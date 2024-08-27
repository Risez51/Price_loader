import resultItem, fileWorker, spotter


class Parser_m2_id:
    def __init__(self):
        print('\nМ2_ИД - старт обработки.')
        self.url_xml_file = 'https://instrument.ru/api/personalFeed/2457863858affb21377a5232617d828c/'
        #self.url_xml_file = '/home/rid/PycharmProjects/Price_loader/123.xml'

    def parse(self):
        file_reader = fileWorker.FileReader()
        xml_file = file_reader.get_xml_file(self.url_xml_file)
        #xml_file = file_reader.get_local_xml_file(self.url_xml_file)
        return self.get_result_list_from_xml(xml_file)

    def get_result_list_from_xml(self, xml_file):
        item_list = xml_file.getElementsByTagName('offer')
        result_list = []
        for item in item_list:
            status = item.getAttribute('available')
            params = item.getElementsByTagName('param')
            result_item = resultItem.ResultItem()

            if status == "true":
                for param in params:
                    if param.getAttribute('name') == 'Бренд':
                        result_item.brand = param.firstChild.nodeValue

                for node in item.childNodes:
                    if node.nodeType == 1:
                        if node.tagName == 'sku':
                            result_item.article = str(node.firstChild.data)
                        if node.tagName == 'price':
                            result_item.purchase_price = ((float(node.firstChild.data)/1.2)*0.84)
                            result_item.selling_price = (float(node.firstChild.data)*0.945)
                        if node.tagName == 'name':
                            result_item.name = str(node.firstChild.data)
                            result_item.site_name = str(node.firstChild.data)
                        if node.tagName == 'available':
                            if str(node.firstChild.data) == "В наличии":
                                result_item.quantity = 10
                            else:
                                result_item.quantity = 0
            if result_item:
                result_list.append(result_item.to_dict())
        return result_list
