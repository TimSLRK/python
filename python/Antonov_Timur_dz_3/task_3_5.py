from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_tokes(num):
    """ Makes a list of jokes from three random words.

    Arguments:
    num -- the number of jokes the user wants to make.
    """
    joke_list = []
    for i in range(num):
        joke = f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
        joke_list.append(joke)
    return joke_list


print(get_tokes(8))