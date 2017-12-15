# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# i = 1
# f = 1.3
# s = 'str'
# b = True
# None

# list = ['a','b','c']
# 有序，append()，pop(index)，insert(index,value)

# tuple = ('a','b','c'，['d','e'])
# 初始化即不可更改，仅一个元素必须加个逗号

# dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 无序，key in dict，dict.get(key,notFoundResponse)，pop(key)

# set = set([1, 2, 3])
# 无序，自动去重，用list创建，add(key)，remove(key)，s1 & s2，s1 | s2

# print("enter your name")
# name = input()
# print("enter your birth year",name)
# year = int(input())
# print(name,"you are",2017-year,"years old")

# w = float(input("输入体重：（单位：千克）"))
# h = float(input("输入身高：（单位：米）"))
# b = w/h/h
# if b>32:
#   r="严重肥胖,%.2f" % b
# elif b>=28:
#   r="肥胖,%.2f" % b
# elif b>=25:
#   r="过重,%.2f" % b
# elif b>=18.5:
#   r="正常,%.2f" % b
# else:
#   r="过轻,%.2f" % b
# print(r)

# sum = 0
# for x in range(2,101):
#   sum = sum +x
# print(sum)

# sum = 0
# n = 100
# while n>0:
#   sum = sum+n
#   n = n-1
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#   print('hello, %s,and hello %s' % (x,x))

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(hex(n2))

# 在交互环境中引入函数
# from filename import funcname

# def my_abs(x):
#   if not isinstance(x, (int, float)):
#     raise TypeError('bad operand type')
#   if x >= 0:
#     return x
#   else:
#     return -x

# import math
# def move(x,y,step,angle=0):
#   nx = x + step*math.sin(angle)
#   ny = y + step*math.cos(angle)
#   return nx,ny

# 二元一次方程求解
# import math
# # ax*x + bx + c = 0
# def findX(a,b,c):
#   if a<=0:
#     return
#   delta = b*b-4*a*c
#   if delta<0:
#     return "无解"
#   else:
#     x1 = (-b+math.sqrt(b*b-4*c*a))/(2*a)
#     x2 = (-b-math.sqrt(b*b-4*c*a))/(2*a)
#     return x1,x2

# 多个数n次方的和
# def sum_power(*numbers,n=2):
#   r = 0
#   for x in numbers:
#     m = n
#     s = 1
#     while m>0:
#       m = m-1
#       s = s*x
#     r = r+s
#   return r

# 1 位置参数，func(a,b)，必送，顺序
# 2 默认参数，func(a,b=1,c=2)，可选，一定在位置参数之后，必须指向不变对象(数，串，none)
#    func(a,b)或func(a,c=2)
# 3 可变参数， func(a,*b)，*b指示0或多个参数，组装成tuple使用
# 4 命名关键字参数，func(a,*,key1,key2=default2)或func(a,*b,key1,key2),*号或者可变参数分隔
#   func(a,*,key1=value1,key2=value2)
# 5 关键字参数，func(a,**b)，**b指示0或多个带参数名的参数，组装成dict使用
# 传参不会影响原数据

# 汉诺塔，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
# def move(n,a,b,c):
#   if n==1:
#     print(a,'->', c)
#   else:
#     move(n-1,a,c,b)
#     print(a,'->', c)
#     move(n-1,b,a,c)

# 切片，a = b[:]  复制，对不变对象等同=直接复制，对可变对象不同

# 生成器，用()的生成式
# 斐波那契数列
# def fib(max):
#   n, a, b = 0, 0, 1
#   while n < max:
#     yield b    # yield b就是函数生成器
#     a, b = b, a + b
#     n = n + 1
#   return 'done'

# 注意，赋值语句：
# a, b = b, a + b
# 相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

# 打印 杨辉三角
#       1
#     1   1
#     1   2   1
#   1   3   3   1
#   1   4   6   4   1
# 1   5   10  10  5   1
# def triangles(a):
#   L=[1]
#   for i in range(0,a):
#     yield L
#     L=[1]+[L[j]+L[j+1] for j in range(len(L)-1)]+[1]
# for a in triangles(11):
#   print(a)

# 字符串转数字
# 整数
# from functools import reduce
# def str2int(s):
#   def fn(x, y):
#     return x * 10 + y
#   def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#   return reduce(fn, map(char2num, s))
# print(str2int('123456'))
# 浮点
# from functools import reduce
# import math
# def str2float(s):
#   ls = s.split('.')
#   def fn(x, y):
#     return x * 10 + y
#   def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#   index = s.index('.')
#   return reduce(fn, map(char2num, ls[0])) + reduce(fn, map(char2num, ls[1])) / math.pow(10, len(ls[1]))
# print('str2float(\'12345.6\') =', str2float('12345.6'))

# def _odd_iter():
#   n = 1
#   while True:
#     n = n + 2
#     yield n
# def _not_divisible(n):
#   return lambda x: x % n > 0
# def primes():
#   yield 2
#   it = _odd_iter() # 初始序列
#   while True:
#     n = next(it) # 返回序列的第一个数
#     yield n
#     it = filter(_not_divisible(n), it) # 构造新序列
# def _printPrime(max):
#   # 打印max以内的素数:
#   for n in primes():
#     if n < max:
#       print(n)
#     else:
#       break
# _printPrime(20)

# -*- coding: utf-8 -*-

# 回数，对称数字
# def is_palindrome(n):
#   return str(n) == str(n)[::-1]
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))

# 排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#   # return t[0].lower;  #按人名首字母
#   return t[1];  #按成绩
# L2 = sorted(L, key=by_name)
# print(L2)

# 调用时再运算
# def lazy_sum(*args):
#   def sum():
#     ax = 0
#     for n in args:
#       ax = ax + n
#     return ax
#   return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# f()

# 装饰器
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
# 把@logger("execute")放到now()函数的定义处，相当于执行了语句：now = logger("execute")(now)
# import functools
# def logger(text="run"):
#   def decorator(func):
#     @functools.wraps(func) # 传递now的名字等属性
#     def wrapper(*args, **kw):
#       print('%s %s():' % (text, func.__name__))
#       func(*args, **kw)
#     return wrapper
#   return decorator
# def log(func):
#   @functools.wraps(func) # 传递now的名字等属性
#   def wrapper(*args, **kw):
#     print('%s():' % ( func.__name__))
#     func(*args, **kw)
#   return wrapper
# @log
# def now():
#   print('2015-3-25')
# now()
# @logger("execute")
# def now():
#   print('2015-3-25')
# now()

# 模块
# ' a test module '
# __author__ = 'Michael Liao'
# import sys
# print(sys.executable, len(sys.argv))
# def test():
#   args = sys.argv
#   if len(args)==1:
#     print('Hello, world!')
#   elif len(args)==2:
#     print('Hello, %s!' % args[1])
#   else:
#     print('Too many arguments!')
# if __name__=='__main__': # 命令行直接执行时__name__为__main__，被调用时为模块名
#   test()

# 三方库
# from PIL import Image
# im = Image.open('D:\\mygit\\py\\icon.png')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')

# 类和示例
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score

#     def get_name(self):
#         return self.__name

#     def set_name(self, newName):
#         self.__name = newName
#         return

#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))

# bart = Student('Bart Simpson', 60)
# bart.set_name('hi')
# bart.print_score()

# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')
def run_twice(animal):
    animal.run()
    animal.run()
class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')
a = Dog()
a.run()