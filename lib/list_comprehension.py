#!/usr/bin/env python3

def return_evens(sequence):
    return [x for x in sequence if x % 2 == 0]


print(return_evens([0, 1, 3, 5, 7, 8, 9]))

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]


print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))


print(make_exclamation([]))


