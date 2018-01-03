import random
import mysql.connector



def random_authcode(randomlength = 8):
    authcode = ''
    for i in range(randomlength):
        authcode +=(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    return authcode

def get_authcode():
    arr = []
    for i in range(200):
        a = random_authcode()
        arr.append(a)
    return arr

def save_authcode():
    conn = mysql.connector.connect(user='root',password = '123456',database = 'python')
    cursor = conn.cursor()
    # cursor.execute('create table authcode (id VARCHAR (20) PRIMARY key,authcode VARCHAR (20))')
    arr = get_authcode()
    print(arr)
    for i in range(200):
        cursor.execute('insert into authcode (id, authcode) values (%s, %s)', [i+1, str(arr[i])])
    conn.commit()
    cursor.close()

if __name__=='__main__':
    save_authcode()
