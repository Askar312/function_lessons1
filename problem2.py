def fibonach():
    f1 = 0
    f2 = 1
    n = int(input('Введите необходимое количество чисел для подчета !: '))
    print ('0,', f2, end=', ')
    while n > 2:
        f1, f2 = f2, f1 + f2
        print (f2, end=', ')
        n -= 1

fibonach()