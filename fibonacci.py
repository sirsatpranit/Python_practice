#!/bin/python

number = int(input("Enter the number : "))
sqrt_5 = 5 ** 0.5
fib_number = (((1+sqrt_5)/2)**number-((1-sqrt_5)/2)**number)/sqrt_5
print(f"{number}th element in fibonacci : {int(fib_number)}")
