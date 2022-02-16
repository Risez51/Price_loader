class ResultItem:
    def __init__(self):
        self.article = ''
        self.name = ''
        self.unit = ''
        self.purchase_price = ''
        self.quantity = ''
        self.rrc = ''
        self.roc = ''
        self.brand = ''
        self.selling_price = ''
        self.group_code = ''
        self.site_name = ''
        self.multiplicity = ''

    def to_dict(self):
        return {'Артикул поставщика': self.article,
                'Наименование': self.name,
                'Ед.изм': self.unit,
                'Цена закупки, без НДС': self.purchase_price,
                'Количество': self.quantity,
                'РРЦ': self.rrc,
                'РОЦ': self.roc,
                'Бренд': self.brand,
                'Цена продажи, без НДС': self.selling_price,
                'Код группы': self.group_code,
                'Наименование для сайтов': self.site_name,
                'Кратность поставки': self.multiplicity}
