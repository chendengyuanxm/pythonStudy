import random


class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self) -> str:
        return '(%s, %s)' % (self.color, self.number)

    def __repr__(self):
        return repr((self.color, self.number))


def is_bomb(lst):
    first = lst[0]
    for l in lst:
        if l.number != first.number:
            return False

    return True


def is_same_color_and_sequence(lst):
    return is_same_color(lst) and is_sequence(lst)


def is_same_color(lst):
    first = lst[0]
    for l in lst:
        if l.color != first.color:
            return False

    return True


def is_sequence(lst):
    lst = sorted(lst, key=lambda c: c.number, reverse=True)
    pre = lst[0]
    for l in lst[1:]:
        if l.number != pre.number + 1:
            return False
        pre = l

    return True


def get_two_same_number(lst):
    n = len(lst)
    for i in range(n-1):
        pre = lst[i]
        for j in range(i+1, n):
            nxt = lst[j]
            if pre.number == nxt.number:
                return pre.number

    return None


def is_two_same(lst):
    if get_two_same_number(lst) is not None:
        return True

    return False


def get_level(lst):
    if is_bomb(lst):
        return 1
    if is_same_color_and_sequence(lst):
        return 2
    if is_same_color(lst):
        return 3
    if is_sequence(lst):
        return 4
    if is_two_same(lst):
        return 5

    return 6


def comp_number(lst1, lst2):
    lst1 = sorted(lst1, key=lambda c: c.number, reverse=True)
    lst2 = sorted(lst2, key=lambda c: c.number, reverse=True)

    for i in range(count):
        if lst1[i] != lst2[i]:
            return lst1[i].number - lst2[i].number

    return 0


def comp_level_5_number(lst1, lst2):
    double_number1 = get_two_same_number(lst1)
    double_number2 = get_two_same_number(lst1)
    if double_number1 != double_number2:
        return double_number1 - double_number2

    single_number1 = list(filter(lambda v: v != double_number1, lst1))[0].number
    single_number2 = list(filter(lambda v: v != double_number2, lst2))[0].number
    if single_number1 != single_number2:
        return single_number1 - single_number2

    return 0


def comp(lst1, lst2):
    level1 = get_level(lst1)
    level2 = get_level(lst2)
    sub = level2 - level1
    print(level1, level2, sub)

    if sub != 0:
        return sub

    if level1 == 1:
        return comp_number(lst1, lst2)
    elif level1 == 2:
        return comp_number(lst1, lst2)
    elif level1 == 3:
        return comp_number(lst1, lst2)
    elif level1 == 4:
        return comp_number(lst1, lst2)
    elif level1 == 5:
        return comp_level_5_number(lst1, lst2)
    elif level1 == 6:
        return comp_number(lst1, lst2)


# 生成牌
cards = []
cards1 = [Card('A', n) for n in range(2, 15)]
cards2 = [Card('B', n) for n in range(2, 15)]
cards3 = [Card('C', n) for n in range(2, 15)]
cards4 = [Card('D', n) for n in range(2, 15)]
cards.extend(cards1)
cards.extend(cards2)
cards.extend(cards3)
cards.extend(cards4)
random.shuffle(cards)
print(cards)

# 发牌
count = 3
peoples = 5

delivered_cards = []
for i in range(peoples):
    p_card = []
    for n in range(count):
        c = random.choice(cards)
        cards.remove(c)
        p_card.append(c)
    delivered_cards.append(p_card)
print(delivered_cards)

# 比大小
# r = comp(delivered_cards[0], delivered_cards[1])
n = len(delivered_cards)
for i in range(n-1):
    for j in range(i, n):
        if comp(delivered_cards[i], delivered_cards[j]) > 0:
            temp = delivered_cards[i]
            delivered_cards[i] = delivered_cards[j]
            delivered_cards[j] = temp
print(delivered_cards)
