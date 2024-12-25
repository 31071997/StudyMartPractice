# -*- coding: utf-8 -*
"""
Created on Wed Dec 25 14:27:56 2024

@author: ASUS
"""
def ListSum(input_nunmbers):
    add = 0
    for i in input_nunmbers:
        i = int(i) 
        add += i
    return add
num = input().split()
series = []
for i in num:
    series.append(i)
print(ListSum(series))