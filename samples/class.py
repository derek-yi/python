# coding=gbk

#import os
#import sys

class MY_CLASS:
    def __init__(self, str, num):
        self.str = str
        self.num = num

    def process(self, str, num):
        print(self.str+str, self.num+num)
		
my_class = MY_CLASS("sum", 100)
my_class.process(" is",111)
