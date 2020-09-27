import json
import csv

class Moneda:
    def __init__(self,id,name,value1,value2):
        self.id=id
        self.name = name
        self.value1 = value1
        self.value2 = value2

    def set_id(self, id):
        self.__id = id
        if id > 0:
            return id

    def set_name(self, name):
        self.__name = name
    
    def set_value1(self, value1):
        self.__value1 =  value1 

    def set_value2(self, value2):
        self.__value2 =  value2

    def get_name(self):
        return self.__name
    
    def get_value1(self, value1):
        return self.__value1 

    def get_value2(self, value2):
        return self.__value2

    @staticmethod
    def convert_json_data(path_file):
        
        print('Iniciando csv file')
        with open(path_file, "r") as csvfile:
            data_csv = csv.DictReader(csvfile)
            for row in data_csv:
                data = (dict(row))
                print(data)
            return data

    @staticmethod 
    def generate_json(monedas_list):
        key =['id','value1','value2','name']
        moneda_list = []
        for item in moneda_list:
            m = {}
           
            k = key[0]
            v = int(item.get_id())
            m[k]=v
            
            k = key[1]
            v = float(item.get_value1())
            m[k]=v

            k = key[2]
            v = float(item.get_value2())
            m[k]=v

            k = key[3]
            v = item.get_divisa_name()
            m[k]=v
            moneda_list.append(m)
        moneda =json.dumps(moneda_list)
        return moneda




        
