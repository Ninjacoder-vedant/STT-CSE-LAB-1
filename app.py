"""This module performs calculations of 2 operands"""
print("----Calculator----")
print("Enter the digits")
a = float(input())
b = float(input())
print("Enter the operation you want to perform (+,-,/,*)")
op = input()
if op=="+" :
    print(a+b) 
elif op=="-":
    print(a-b)
elif op=="/":
    print(a/b)
else:
    print(a*b)
