def revers():
    list_1 = ['name', 'age', '1', '19']
    a = list(reversed(list_1[len(list_1)//2:]))
    b = list(reversed(list_1[:len(list_1)//2]))
    print(b + a)
revers()