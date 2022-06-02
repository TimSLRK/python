

def thesaurus(*args):
    names = {}
    for name in args:
        names.setdefault(name[0], []).append(name)
    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))




