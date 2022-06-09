tutors = [
'Иван', 'Анастасия', 'Петр', 'Сергей',
'Дмитрий', 'Борис', 'Елена'
]
klasses = [
'9А', '7В', '9Б', '9В', '8Б', '10А'
]


def generator(names, groups):
    """
    Генерирует кортежи, состоящие из имени и
    класса, где обучается ученик.
    :param names: Имя ученика
    :param groups: Класс, где обучается ученик.
    """
    for i in range(len(names)):
        yield (names[i], groups[i])
        if len(names) > len(groups):
            groups.append(None)


gen_tutors_klasses = generator(tutors, klasses)
print(type(gen_tutors_klasses))
for j in range(len(tutors) + 1):
    print(next(gen_tutors_klasses))










