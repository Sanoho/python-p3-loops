#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
    int_list = [int ** 2 for int in int_list]
    return int_list


def fizzbuzz():
    i = 1
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            i = "FizzBuzz"
            print(i)
        elif i % 5 == 0 and i != 0:
            i = "Buzz"
            print(i)
        elif i % 3 == 0 and i != 0:
            i = "Fizz"
            print(i)
        else:
            print(i)
