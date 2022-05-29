price = [12, 25.06, 240, 15, 26.03, 14.76, 29, 56, 87, 20.32, 12.12, 98]
print(id(price))
price.sort()
print(id(price))
for c in price:
    rub = int(c)
    kop = (c - rub) * 100
    print(f'{rub} руб {kop:02.0f} коп', end =', ')
print(id(price))
cost = price[:]
print(cost)
cost.sort(reverse = True)
i = 0
while i < 5:
    print(cost[i])
    i += 1
