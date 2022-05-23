for i in range(1,101):
    if i % 10 == 1:
        print(i, 'процент')
    elif 2 <= i % 10 <= 4 and i // 10 != 1:
        print(i, 'процента')
    else:
        print(i, 'процентов')