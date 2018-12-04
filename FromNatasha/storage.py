import json
import os

#папка с файлами
BASEDBPATH = 'data' #папка
BLOCKFILE = 'blockchain' #файл хранящий содержимое блоков: /data/blockchain.json
TXFILE = 'transactions' #файл, хранящий содержимое транзакций /data/transactions.json


#сюда вообще можно не смотреть. (как вспомогательный шаблон)
class BaseDB():

    filepath = ''

    def __init__(self):
        self.set_path()
        self.filepath = '/'.join((BASEDBPATH, self.filepath))

    def set_path(self):
        pass

    def find_all(self):
        return self.read()

    def insert(self, item):
        self.write(item)

    def read(self):
        raw = ''
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath,'r+') as f:
            raw = f.readline()
        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def write(self, item):
        data = self.read()
        if isinstance(item,list):
            data = data + item
        else:
            data.append(item)
        with open(self.filepath,'w+') as f:
            f.write(json.dumps(data))
        return True

    def clear(self):
        with open(self.filepath,'w+') as f:
            f.write('')

    def hash_insert(self, item):
        exists = False
        for i in self.find_all():
            if item['hash'] == i['hash']:
                exists = True
                break
        if not exists:
            self.write(item)

class BlockChainDB(BaseDB):

    #
    def set_path(self):
        self.filepath = BLOCKFILE

    #последний блок
    def last(self):
        bc = self.read()
        if len(bc) > 0:
            return bc[-1]
        else:
            return []

    #поиск по соответствующему хэшу в блоках
    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    #
    def insert(self, item):
        self.hash_insert(item)

class TransactionDB(BaseDB):
    """
    """
    #
    def set_path(self):
        self.filepath = TXFILE

    #поиск по соответсвующему хэшу в транзакциях
    def find(self, hash):
        one = {}
        for item in self.find_all():
            if item['hash'] == hash:
                one = item
                break
        return one

    #
    def insert(self, transactions):
        if not isinstance(transactions, list):
            transactions = [transactions]
        for transaction in transactions:
            self.hash_insert(transaction)