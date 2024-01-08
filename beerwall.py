#!/usr/bin/env python3

def bottles_of_beer(num):
    if num == 1:
        return print(f"{num} bottle of beer on the wall, {num} bottle of beer.\nTake one down, pass it around, no more bottles of beer on the wall.")
    elif num == 0:
        return ("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        return (f"{num} bottles of beer on the wall, {num} bottles of beer.\nTake one down, pass it around, {num-1} {'bottle' if num-1 == 1 else 'bottles'} of beer on the wall.")

def main():
    for i in range(99, -1, -1):
        print(bottles_of_beer(i))
        print() 
