#!/usr/bin/python3
""" my list function """


class MyList(list):
    """ class of my list """

    def print_sorted(self):
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
