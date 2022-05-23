numbers = []
for i in range(1,1001,2):
    numbers.append(i ** 3)
result = 0
for number in numbers:
    number = str(number)
    digits = number.split()
    total = 0
    for digits in number:
        digits = int(digits)
        total += digits
    if total % 7 == 0:
            result += int(number)
new_numbers = numbers[:]
for j in range(len(new_numbers)):
    new_numbers[j] += 17
new_result = 0
for numeric in new_numbers:
    numeric = str(numeric)
    new_digits = numeric.split()
    new_total = 0
    for new_digits in numeric:
        new_digits = int(new_digits)
        new_total += new_digits
    if new_total % 7 == 0:
        new_result += int(numeric)
print(result, new_result)
