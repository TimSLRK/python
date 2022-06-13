import json
names = [
    'Иванов, Иван, Иваныч \n',
    'Андреев, Андрей, Андреевич \n',
    'Антонов, Антон, Антонович \n',
    'Ульянов, Александр, Александрович'
]
hobby = [
    'скалолазание, охота \n'
    'рыбалка \n'
    'футбол \n'
]
with open('users.csv', 'w', encoding='utf-8') as file_1:
    file_1.writelines(names)

with open('hobby.csv', 'w', encoding='utf-8') as file_2:
    file_2.writelines(hobby)
users_list = []
with open('users.csv', 'r', encoding='utf-8') as file_1:
    for line_1 in file_1:
        users_list.append(line_1.rstrip())

hobby_list = []
with open('hobby.csv', 'r', encoding='utf-8') as file_2:
    for line_2 in file_2:
        hobby_list.append(line_2.rstrip())

person = {}
if len(users_list) >= len(hobby_list):
    for i in range(len(users_list)):
        person[users_list[i]] = hobby_list[i]
        hobby_list.append(None)
else:
    for j in range(len(users_list)):
        person[users_list[j]] = hobby_list[j]
    exit(1)
person_ser = json.dumps(person)
with open('person.json', 'w', encoding='utf-8') as file_3:
    file_3.write(person_ser)

#Здесь проверка на то, что в Питоне текст будет отображаться правильно!
with open('person.json', 'r', encoding='utf-8') as f:
    test = f.read()
humans = json.loads(test)
print(humans)










