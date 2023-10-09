#!/usr/bin/python3
""" my list function that sort matrix """


class MyList(list):
    """ class of my list to be initiate """

    def print_sorted(self):
        """ print sorted defined """
        sorted_list = sorted(self)
        print("{}".format(sorted_list))
