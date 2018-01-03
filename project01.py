import random



def random_authcode(randomlength = 8):
    authcode = ''
    for i in range(randomlength):
        authcode +=(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'))
    return authcode

def get_authcode():
    arr = []
    for _ in range(200):
        a = random_authcode()
        arr.append(a)
    print(arr)






if __name__=='__main__':
    get_authcode()
