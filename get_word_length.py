#!/usr/bin/python

import os

def getWordLength(text):

    t = text
    word_length = {}
    words = t.split()
    for word in words:
        word_length.update({word: len(word)})

    return word_length


