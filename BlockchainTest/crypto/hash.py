import hashlib
import json
import numpy as np



def hash_block(index, timestamp, data, prev_hash): #возможно, удобнее было бы передавать не инфу, а блок?
    str=(index+timestamp+data+prev_hash).encode('utf-8')
    hash=hashlib.sha256(str).hexdigest()
    return  hash

def read(filepath):
        raw = ''

        with open(filepath, 'r+') as f:
            raw = f.readline()
        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

def write(item , filepath):
        data = filepath.read()
        if isinstance(item, list):
            data = data + item
        else:
            data.append(item)
        with open(filepath, 'w+') as f:
            f.write(json.dumps(data))
        return True

def validate_blockchein(file_path,valid_hash,index, timestamp, info, prev_hash ):
    data=read(file_path)
    print(len(data))
    hash = np.chararray(len(data))
    for i in range(0,len(data)):
        hash[i] = hash_block(data[i]['index'], data[i]['timestamp'], data[i]['nouce'], data[i]['previous_block'])
        if(hash[i]!=data[i+1]['prev_hash']):
            print("Обнаружена ошибка в цепочке хэшей!")
            return False
    return(valid_hash(data, valid_hash,index, timestamp, info, prev_hash))

def validate_hash(data, valid_hash,index, timestamp, info, prev_hash):
    #Если последний хэш в блоке который получился, + информация нового блока == полученному хэшу , то блок валидный
    if(hash[len(data)]== prev_hash):
        if(hash_block(index,timestamp,info,prev_hash)==valid_hash):
            print("Валидация прошла успешно!")
            return True
        else:
            print("Валидация не состоялась!")
            return False

#data=read('blockchain')
#print(data)
#validate_blockchein('blockchain')
