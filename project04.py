import re


def count_words():
    with open('test.txt','r') as f:
        data =f.read()
        m = re.findall('[a-zA-Z]+',data)
        print(len(m))


if __name__=='__main__':
    count_words()

