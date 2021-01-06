#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Mario
class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staff = []

    def enroll(self, stu_obj):
        print("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        self.staff.append(staff_obj)
        print("雇佣了%s" % staff_obj.name)


class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

        def info(self):
            pass


class Tercher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Tercher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def info(self):
        print("""
        ------ info of %s------
        name:%s
        age:%s
        sex:%s
        salary:%s
        course:%s
        """ % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course[%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade, school_obj):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

        self.school = school_obj  # 将School和Student联系在一起,使用:school_obj.xxx

    def info(self):
        print("""
        ------ info of %s------
        name:%s
        age:%s
        sex:%s
        stu_id:%s
        grade:%s
        """ % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paied tuition for %s yuan" % (self.name, amount))


school = School("南昌大学软件学院", "青山湖区")
t1 = Tercher("teacher1", 56, "M", 20000, "计算机基础")
t2 = Tercher("teacher2", 35, "F", 14800, "python")
s1 = Student("student1", 19, "F", 1001, "信息安全1班")
s2 = Student("student2", 19, "M", 1038, "信息安全2班")
t1.info()
s1.info()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)
print(school.students)
print(school.staff)
school.staff[0].teach()
for stu in school.students:
    stu.pay_tuition(5000)
