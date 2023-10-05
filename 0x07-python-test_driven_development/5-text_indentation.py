#!/usr/bin/python3
""" This code print two lines after some character """


def text_indentation(text):
    """ Function that prints a text with 2 new lines """    
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        text = text.strip()
        for char in text:
            print(char, end="")
            if char in '.?:':
                print('\n\n', end="")
        print()
