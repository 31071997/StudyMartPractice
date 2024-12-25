# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 12:31:12 2024

@author: ASUS
"""
print("Enter your marks: ")
marks = input().split()
results = []
for i in marks:
    i = int(i)
    if(i < 25):
        results.append("F")
    elif(i < 45):
        results.append("E")
    elif(i < 50):
        results.append("D")
    elif(i < 60):
        results.append("C")
    elif(i < 80):
        results.append("B")
    elif(i < 90):
        results.append("A")
    else:
        results.append("A+")
print(results)    