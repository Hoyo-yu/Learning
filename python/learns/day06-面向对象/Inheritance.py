#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
# 继承
# class People：#经典类
class People(object):  # 新式类与通经典类的区别主要体现在多继承的顺序问题

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = []  # 添加一个默认的空朋友列表,为实例化对象
        # 实例变量在发生改变时,调用类其他继承类里面的方法时,有该实例变量的值也会相应的发生变化

    def eat(self):
        print("%s is eating" % self.name)

    def talk(self):
        print("%s is talking" % self.name)

    def sleep(self):
        print("%s is sleeping" % self.name)


class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))
        # self.friends.append(obj.name)# 此时的obj.name为一个字符串
        self.friends.append(obj)  # 这里obj为实例化对象,绑定了它的实例变量,当实例对象的值发生改变时,make_friends里面的obj.name也与之改变


class Man(Relation, People):  # 最好将带有构造函数的类放在前面
# 后面使用构造函数时,按顺序查找,如果继承的第一个类里有构造函数,后面的构造函数不会使用
# class Man(People,Relation): # 先People后Relation,多继承
    # def __init__(self, name, age, money):  # 重构父类的方法,新增实例变量
    #     # People.__init__(self, name, age)  # 调用父类的实例变量
    #     super(Man, self).__init__(name, age)  # 等同于上面的语句,新式类写法,按照继承顺序使用构造函数内的实例变量
    #     self.money = money  # Man这个类独有的、私有的实例变量
    #     print("%s一出生就有%s money" % (self.name, self.money))

    def whoring(self):
        print("%s is whoring" % self.name)

    def sleep(self):
        # People.sleep(self) #未注释的情况下,对父类方法添加新内容
        print("man is sleeping")  # 重写父类的方法


class Woman(People, Relation):
    def bearing(self):
        print("%s was borned a baby last weekend" % self.name)


m1 = Man("Mario", 24)
# m1.talk()
# m1.whoring()
# m1.sleep()

w1 = Woman("cxm", 23)
# w1.bearing()

m1.make_friends(w1)
# Relation类在People前,虽然name属性在People类里,但是Relation没有name属性就会去People里找,此时的name实例对象已经在上述实例化的时候产生了
# 所以在执行make_friend方法时已经有name这个属性了,所以不会报错

w1.name = "lll"  # 将w1改名为lll
m1.make_friends(w1)
# 所以上面的self.friends.append(obj.name)--"这个为字符串"--应该改为self.friends.append(obj)--"这个为对象,name与之绑定了"--
print(m1.friends[0].name)  # 此时的m1.friend[0]为w1,也就是将默认的空对象新加了w1这个实例化对象
# 如果上面的为self.friends.append(obj.name),他的朋友一直是cxm,并不是改名后的lll
