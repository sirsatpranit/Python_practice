#!/bin/python3

def is_isogram(string):
    return len(set(string.lower())) == len(string)


string = input("Enter string : ")
print(is_isogram(string))
