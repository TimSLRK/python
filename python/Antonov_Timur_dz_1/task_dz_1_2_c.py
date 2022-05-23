numbers = []
for i in range(1,1001,2):
    numbers.append(i ** 3)
total = 0
for number in numbers:
    order = 0
    num = number
    while number != 0:
        digit = number % 10
        order += digit
        number //= 10
    if order % 7 == 0:
        total += num
for j in range(len(numbers)):
    numbers[j] += 17
total_with_sum = 0
for numeric in numbers:
    order_with_sum = 0
    num_with_sum = numeric
    while numeric != 0:
        digit_with_sum = numeric % 10
        order_with_sum += digit_with_sum
        numeric //= 10
    if order_with_sum % 7 == 0:
        total_with_sum += num_with_sum
print(total, total_with_sum)