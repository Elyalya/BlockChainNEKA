# crypto
Криптография для криптовалюты

Файл 1. CryptoKey.py
Используется для генерации публичного ключа, приватного ключа и адреса владельца кошелька.
Пример использования функций:
Создание публичного ключа :
pk=PrivateKey() 
Чтобы использовать его , нужно вызвать функцию которая возвращает ключ в строковом формате
p=PrivateKeyStr(pk)
Для генерации публичного ключа:
k=PublicKey(pk) используем не преобразованный закрытый ключ, функция возвращает открытый строкой
 Здесь встроена функция связи с центром сертификации , которая проверяет ключ на уникальность
 Для получения адреса:
a=Address(p) возвращает адрес в строковом формате
Остальные функции используются в качестве вспомогательных, для реализации алгоритмов.
Файл 2.hash.py
def hash_block(index, timestamp, data, prev_hash)- функция создания хэша блока из информации блока и предыдущего хэша
def validate_blockchein(file_path,valid_hash,index, timestamp, info, prev_hash )- функция проверки блокчейна , считывает из файла 'blockchein' всю цепочку хэшей, проверяет их, и если все в порядке проверяет новый хэш и возвращает true
Аргументы:
file_path- путь к файлу где хранятся хэши,valid_hash - хэш который нужно проверить ,(index , timestamp, info, prev_hash )-информация блока
Пример использования:
data=read('blockchain') #не обязательно
print(data)#не обязательно
validate_blockchein('blockchain')
Файл 3. sertif_center.py
Осуществляет функции сертификационного центра
def check_publickey(public_key) - проверяет хэш на уникальность
def check_write(public_key)- проверяет  и записывает (лучше использовать ее)
def read_file()- читает файл с ключами
def show_keys() - для просмотра ключей
def write_to_file(public_key) - дописывает ключ в файл
