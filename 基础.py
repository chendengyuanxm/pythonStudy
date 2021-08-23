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