# Encapsulating variables

class DataBase:
    def __init__(self):
        self.__data = {}  # The __ makes the attribute private

    @property
    def get_data(self):
        return self.__data

    def insert_client(self, id, name):
        if 'client' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def del_client(self, id):
        del self.__data['clients'][id]

    def clients_list(self):
        for id, name in self.__data['clients'].items():
            print(id, name)


datb = DataBase()
datb.insert_client(1, 'Kevin')

datb.clients_list()
