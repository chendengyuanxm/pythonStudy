import random

members = list(range(0, 300))
total = len(members)
print(members)

awards = [
    {
        'level': 1,
        'amount': 3,
        'desc': '泰国5日游'
    },
    {
        'level': 2,
        'amount': 6,
        'desc': 'iphone手机'
    },
    {
        'level': 3,
        'amount': 30,
        'desc': '避孕套一盒'
    },
]
print(awards)

# 抽奖
for award in awards:
    total = len(members)
    level = award['level']
    amount = award['amount']
    desc = award['desc']
    lottery_pool = [level for x in range(0, amount)] + [0 for x in range(0, total - amount)]
    random.shuffle(lottery_pool)

    i = 0
    for l in lottery_pool:
        if i >= len(members):
            break
        while members[i] is None:
            i += 1
        if l == level:
            print('恭喜%d号获得%d等奖, 获得奖品%s' % (i+1, level, desc))
            members[i] = None
        i += 1