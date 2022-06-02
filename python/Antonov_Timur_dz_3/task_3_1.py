

def num_translate(num):
    digits = {"zero": "ноль", "one": "один", "two": "два", "three": "три",
              "four": "четыре", "five": "пять", "six": "шесть", "seven": "семь",
              "eight": "восемь", "nine": "девять", "ten": "десять"
              }
    for key, value in digits.items():
        if num == key:
            return value
print(num_translate("one"))



