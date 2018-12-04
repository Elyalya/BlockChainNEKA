#РАСШИРЕНИЕ ЦЕПОЧЕК
'''Что мне понадобится?
 1) создать класс блоков
2) проверить подлинность транзакций (узнать из чего состоит, вытащить хэши)
3) проверить валидность (текущего и следующего блока(?))
4) есть ли право создания блоков (другими словами, майнинг, придумать какое-то условие (у биткоина это угадывание случайного числа)
НАТАШЕ надо передавать блоки, которые она будет хранить
'''

import time
import json

import crypto.hash as hashAl
#import FromNatasha.storage as fileNat
from FromNatasha.storage import BlockChainDB as FileNat
from FromNatasha.storage import TransactionDB as TransNat

class Block:
    '''в этом классе необходимо сделать следующие методы:
    1) создание уникального хэша блока (с помощью библиотеки Альбины?)
    2)
    '''
    #каждый блок должен быть привязанк предыдущему по уникальному хэшу
    def __init__(self, index, timestamp, data, prev_hash):
        #index - номер блока, timestamp - когда блок был создан
        #data -данные(инфа о тразакциях) prevhash - предыдущий хэш
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = prev_hash
        self.hash = self.hashblock()

    def hashblock(self):
        '''кодируем информацию блока и возвращаем хэш с пом. библиотеки Альбины'''
        # создаем хэш информации о новом блоке, включая хэш предыдущего блока и информацию в самом блоке
        hash = hashAl.hash_block(str(self.index), str(self.timestamp), str(self.data), str(self.previous_hash))
        return hash

def create_first_block():
    '''Для создания нового блока. ему нужен хэш предыдущего. Первыйблок не знает хэш
    предыдущего, поэтому его нужно создать руками (нулевой индекс и произвольный хэш)'''
    return Block(0, time.time(), {"proofik": 1,"transactions": None}, hashAl.hash_block(str(0),str(time.time()),str({"proofik": 1,"transactions": None}),str(0))) #какой хэш у первого?

print(hashAl.hash_block(str(0),str(time.time()),str({"proofik": 1,"transactions": None}),str(0)))
firstBlock=create_first_block()

BLOCKCHAIN = [] #будущая цепочка, т.е blockchain
BLOCKCHAIN.append(create_first_block()) #создали первый блок

#новый блок, то есть расширение цепочки, происходит тогда, когда выполняется какое-то условие
#в биткоин это угадывание какого-то числа
#таким образом, необходимо создать функцию, которая будет проверять произошло ли какое-то условие - т.е. доказательство

#ИДЕЯ - брать предыдущий факт доказательства - число и находить следующее делящееся на него число
def proofik(last_proof, blockchain): #ВОПРРОс - для доказательства передавать блок или цепочку? (скорее, цепочку)

  '''inc = last_proof + 1 #переменная, которая будет использоваться для проверки работы

  start_time = time.time()  #время начала
  # Продолжаем увеличивать inc до тех пор, пока он не будет равен числу, которое
  # делится на число, доказывающее работу предыдущего блока
  while not (inc % last_proof == 0):
    inc += 1
    start_time = time.time()
    # (мб сравнивать текущее время с временем старта)
    # тут условие, что если нашли, прекращаем проверку, пришли к консенсусу,
    # иначе возвращаем false?? т.к кто-то другой нашел первым

  return (inc, block) # если число найдено, можно вернуть его как доказательство'''
  # Создаем переменную, которая будет использоваться для проверки работы
  incrementor = last_proof + 1
  # Получаем время начала
  start_time = time.time()
  # Продолжаем увеличивать инкрементатор до тех пор, пока он не будет равен числу, которое
  # делится на простое число
  while not (incrementor % 12421 == 0):
      incrementor += 1
      start_time = time.time()
      # Каждые 60сек проверяем, нашла ли нода подтверждение работы
      if (int((time.time() - start_time) % 60) == 0):
          # Если нашла - прекращаем проверку
          new_blockchain = consensus(blockchain)
          if new_blockchain != False:
              # (False:другая нода первая нашла подтверждение работы)
              return (False, new_blockchain)
  # Как только число найдено, можно вернуть его как доказательство
  return (incrementor, blockchain)


def consensus(blockchain):
    # Если наша цепочка не самая длинная, то мы сохраняем самую длинную цепочку
    # Если самая длинная цепочка не наша, делаем ее самой длинной
    # Ищем подтверждение
    # Получаем блоки с других компьютеров
    other_chains = find_new_chains()

    BLOCKCHAIN = blockchain
    longest_chain = BLOCKCHAIN
    for chain in other_chains:
        if len(longest_chain) < len(chain):
            longest_chain = chain

    if longest_chain == BLOCKCHAIN:
        # Продолжаем искать подтверждение
        return False
    else:
        # обновляем цепочку и ищем снова
        BLOCKCHAIN = longest_chain
        return BLOCKCHAIN

def find_new_chains():
    # данные о других цепочках
    # нужно брать из json все цепочки
    other_chains = []
    for i in range(100): #ИЗМЕНИТЬЬЬЬЬ
            # необходимо счить из json цепочки

            # преоброзавать в словарь
            block = json.loads(block)
            # проверить валидность
            validated = hashAl.validate_blockchein("file_path",str(block.hash),str(block.index), str(block.timestamp), str(block.data), str(block.previous_hash))
            if validated == True:
                # добавляем ее в наш список
                other_chains.append(block)
    return other_chains

#дальше уже должна быть функция майнинга
#НЕОБХОДИМО ПРОВЕРИТЬ ДОКАЗАТЕЛЬСТВО РАБОТЫ, ЗАТЕМ ВАЛИДНОСТЬ И ЗАТЕМ ДОБАВЛЯЮ В СЛОВАРИК json

def mine(blockchain, pending_transactions):
    BLOCKCHAIN = blockchain
    PENDING_TRANSACTIONS = pending_transactions
    while True:
        # последнее доказательство

        last_block = BLOCKCHAIN[len(BLOCKCHAIN) - 1]
        last_proof = last_block.data['proofik']
        #  доказательство работы в текущем блоке
        # ждем пока новое подтверждение не будет найдено
        proof = proofik(last_proof, BLOCKCHAIN)
        # доказательство не нашлось, начинаем майнить опять
        if proof[0] == False:
            # обновляем блокчейн и сохраняемся в файл
            BLOCKCHAIN = proof[1]
            ToJSONFile = FileNat()
            ToJSONFile.insert(BLOCKCHAIN)#send(BLOCKCHAIN)
            continue
        else:
            # когда найдем действительное доказательство работы, мы можем разбить блок,
            # и добавить транзакцию
            # загружаем все ожидающие транзакции и отправляем их
            TransToJSONNat=TransNat()
            PENDING_TRANSACTIONS = TransToJSONNat.find()#????
            PENDING_TRANSACTIONS = TransToJSONNat.insert(PENDING_TRANSACTIONS)
            #  добавляется вознаграждение за майнинг
            PENDING_TRANSACTIONS.append(
                {"from": "NEKA-coin",
                 "amount": 1}
            )
            # необходимо собрать данные для создания нового блока
            new_block_data = {
                "proofik": proof[0],
                "transactions": list(PENDING_TRANSACTIONS)
            }
            new_block_index = last_block.index + 1
            new_block_timestamp = time.time()
            last_block_hash = last_block.hash
            # опустошаем списов
            PENDING_TRANSACTIONS = []
            # создаем новый блок
            mined_block = Block(new_block_index, new_block_timestamp, new_block_data,
                                last_block_hash)
            BLOCKCHAIN.append(mined_block)

            print({
                "index": new_block_index,
                "timestamp": str(new_block_timestamp),
                "data": new_block_data,
                "hash": last_block_hash
            })
            ToJSONFile.insert(BLOCKCHAIN)


