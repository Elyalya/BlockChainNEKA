def check_publickey(public_key):
    database=read_file()
    for i in range(len(database)):
        if(database[i]==public_key):
            return False
def check_write(public_key):
    database=read_file()
    for i in range(len(database)):
        if(database[i]==public_key):
            return False
    write_to_file(public_key)
    return True

def write_to_file(public_key):
    #database=open('keys','r+')
    with open('keys.txt', 'a') as f:
       f.write('\n'+public_key)
    f.close()
    return True
def read_file():

    with open('keys.txt', "r") as file:
        text = file.read().split('\n')
    file.close()
    return text
def show_keys():
    text=read_file()
    print(text)

