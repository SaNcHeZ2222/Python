from random import randint


def get_jokes(how):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(how):
        print(nouns[randint(0, len(nouns) - 1)], adverbs[randint(0, len(adverbs) - 1)], adjectives[randint(0, len(adjectives) - 1)])


get_jokes(2)