import parser_torg_7
import parser_kvt_sitomo
import parser_a4_id
import parser_m2
import fileWorker


def main():
    main_test()
    #print(123)

def main_test():
    fileWorker.FileWriter().check_folder()
    torg_7_result = parser_torg_7.Parser_torg_7().parse()
    fileWorker.FileWriter(0, 'торг7_ЧК').to_excel(torg_7_result)
    kvt_sitomo_result = parser_kvt_sitomo.Parser_kvt_sitomo().parse()
    fileWorker.FileWriter(0, 'КВТ_СИТ').to_excel(kvt_sitomo_result)
    a4_result = parser_a4_id.Parser_a4_id().parse()
    fileWorker.FileWriter(0, 'А4_ИД').to_excel(a4_result)
    input('Для выхода введите любой символ: ')

def parse_m2():
    #fileWorker.FileWriter().check_folder()
    m2_result = parser_m2.Parser_m2_id().parse()
    fileWorker.FileWriter(0, 'М2_ИД').to_excel(m2_result)

if __name__ == '__main__':
    parse_m2()

