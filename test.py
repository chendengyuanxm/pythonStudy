import math
import random

a = 10
b = 3
print(a % b)
print(a // b)
print(a ** b)

if a is b:
    print('')
elif a == b:
    print('')
elif a > b:
    print('')
else:
    print('')

if a > 10 or a < 3:
    print('')

c = int('10', 16)
d = c + 2
print(d)

print(math.sqrt(d))

# random
ls = [1, 2, 3, 4, 5]
r1 = random.choice(ls)
print(r1)
r2 = random.random()
print(r2)

t1 = tuple(['aa', 'bb', 'cc'])
t2 = tuple('bb')
t3 = ('cc', 'dd')
print(t3.count('c'))

dict1 = {
    'name': 'devin',
    'age': 19,
}
print(dict1)
print(dict1.copy())
print(dict1.get('name'))
print(dict1.items())


import time
localtime = time.localtime(time.time())
print(localtime)
print(time.asctime(localtime))
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))


import calendar
cal = calendar.month(2021, 8)
print(cal)
print(dir(calendar))


# str1 = input('please input: ')
# print('content: ' + str1)

try:
    fo = open('aa.txt', 'w')
    print(fo.name)
    print(fo.mode)
    # fo.write('www.baidu.com. hello world')
    line = fo.read(10)
    line = fo.readline()
    print(line)
    fo.close()
except IOError as err:
    print("io error")
    print(err)
except (EOFError, OSError):
    print('eof error')
else:
    print('unknow error')
finally:
    print('finally')


class Test:
    count = 0
    __v = 1

    def __int__(self, name, age):
        self.name = name
        self.age = age


class Parent:
    def __init__(self):
        print('parent')

    def parent_method(self):
        print('parent method')


class Child(Parent):
    def parent_method(self):
        print('override parent method')


print('__doc__: %s' % Test.__doc__)
print('__name__: %s' % Test.__name__)
print('__dict__: %s' % Test.__dict__)
test = Test()
print(test.count)
print(test._Test__v)
