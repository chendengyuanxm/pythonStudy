import logging
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Sun.value)


class ListMetaclass(type):
    def __new__(cls, name, bases, attr):
        attr['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attr)


class MyList(list, metaclass=ListMetaclass):
    pass


l = MyList()
l.add(1)
print(l)

logging.info('hello world')


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ret = ListNode()
    count = 0
    tmp = ret
    while l1 or l2 or count:
        if l1:
            count += l1.val
            l1 = l1.next
        if l2:
            count += l2.val
            l2 = l2.next
        count, val = divmod(count, 10)
        tmp.next = ListNode(val)
        tmp = tmp.next
    return ret.next