import random
__version__ = "2.0"

list_vowel = ['a', 'е', 'i', 'o', 'u', 'y']
list_consonant = ['w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
def consonant(count, ending=''):
    ab = []
    for i in range(1, count + 1):
        ost = float(i) % 2
        if ost == 0:
            ab.append(random.choice(list_vowel))
        else:
            ab.append(random.choice(list_consonant))
    ab.append(ending)

    word = ''.join(ab)
    return word


def vowel(count, ending=''):
    ab2 = []
    for i in range(1, count + 1):
        ost = float(i) % 2
        if ost == 0:
            ab2.append(random.choice(list_consonant))
        else:
            ab2.append(random.choice(list_vowel))
    ab2.append(ending)

    word = ''.join(ab2)

    return word






def vowel(count, ending=''):
    ab2 = []
    for i in range(1, count + 1):
        ost = float(i) % 2
        if ost == 0:
            ab2.append(random.choice(list_consonant))
        else:
            ab2.append(random.choice(list_vowel))
    ab2.append(ending)

    word = ''.join(ab2)

    return word


