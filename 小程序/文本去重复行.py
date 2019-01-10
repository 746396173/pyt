# coding=utf-8
import os

value = set()
with open("抖音url","r",encoding='utf-8') as f:
    line = f.readline()
    while line:
        #line = line.replace("\n","")
        value.add(line)
        line = f.readline()
with open("抖音urlfruit","w",encoding='utf-8') as f:
    for val in value:
        f.write(val)

print(value)