class ResultItem:
    def __init__(self):
        self.article = ''
        self.name = ''
        self.unit = ''
        self.purchase_price = 0
        self.quantity = ''
        self.rrc = ''
        self.roc = ''
        self.brand = ''
        self.selling_price = 0
        self.group_code = ''
        self.site_name = ''
        self.multiplicity = ''
        self.photo_url = ''

    def __str__(self):
        return f'Артикул: {self.article}\n' \
               f'Наименование: {self.name}\n' \
               f'Цена закупки: {self.purchase_price}'

    def to_dict(self) -> dict:
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
