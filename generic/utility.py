from pyjavaproperties import Properties
import openpyxl

class Utility:
    @staticmethod
    def get_property(path,key):
        p = Properties()
        p.load(open(path))
        value=p[key]
        print(f'reading from property file, key: {key}, value: {value}')
        return value

    @staticmethod
    def get_xl_data(path,sheet,row,col):
        print('get data from xl')
        value=''
        try:
            wb=openpyxl.load_workbook(path)
            value = wb[sheet].cell(row, col).value
            wb.close()
            print('able to get the data from xl:', value)
        except:
            print('error while reading xl')
            value=''
        return value