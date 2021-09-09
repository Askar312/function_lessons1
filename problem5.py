from random import choices
num = [0,1,2,3,4,5,6,7,8,9]
cod = [444]
cod.insert(0, 0)

def gen_number():
    choose = choices(num, k=6)
    num1 = (cod + choose)
    replced = str(num1).replace(',', '')
    joined = replced.replace(' ', '')
    print(joined)

gen_number()