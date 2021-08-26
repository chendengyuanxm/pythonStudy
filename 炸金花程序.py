import random


class Card:

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __str__(self) -> str:
        return '(%s, %s)' % (self.color, self.map_number)

    def __repr__(self):
        return repr("%s%s" % (self.color, self.map_number(self.number)))

    @staticmethod
    def map_number(number):
        if number == 14:
            return 'A'
        elif number == 13:
            return 'K'
        elif number == 12:
            return 'Q'
        elif number == 11:
            return 'J'
        return number


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
        if pre.number == 14 and l.number == 2:
            return True
        elif l.number != pre.number + 1:
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


def get_level_name(lst):
    level = get_level(lst)
    if level == 1:
        return '炸弹'
    elif level == 2:
        return '同花顺'
    elif level == 3:
        return '同花'
    elif level == 4:
        return '顺子'
    elif level == 5:
        return '对子'
    elif level == 6:
        return '普通牌'


# 生成牌
cards = []
cards1 = [Card('♡', n) for n in range(2, 15)]
cards2 = [Card('♥', n) for n in range(2, 15)]
cards3 = [Card('♣', n) for n in range(2, 15)]
cards4 = [Card('♢', n) for n in range(2, 15)]
cards.extend(cards1)
cards.extend(cards2)
cards.extend(cards3)
cards.extend(cards4)
random.shuffle(cards)
print('洗牌-->\n', cards)

# 发牌
count = 3
peoples = 5

print('发牌-->')
delivered_cards = []
for i in range(peoples):
    p_card = []
    for n in range(count):
        c = random.choice(cards)
        cards.remove(c)
        p_card.append(c)
    delivered_cards.append({
        'id': i+1,
        'name': '%d号' % (i+1),
        'card': p_card
    })
    print('%s号牌：%s' % (i+1, p_card))

# 比大小
n = len(delivered_cards)
for i in range(n-1):
    for j in range(i, n):
        if comp(delivered_cards[i]['card'], delivered_cards[j]['card']) > 0:
            temp = delivered_cards[i]
            delivered_cards[i] = delivered_cards[j]
            delivered_cards[j] = temp
print('按牌从小到大-->')
for i in delivered_cards:
    print('%s号牌: %s %s' % (i['id'], sorted(i['card'],  key=lambda c:c.number), get_level_name(i['card'])))
