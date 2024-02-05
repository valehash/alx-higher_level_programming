"""This module inherits from the list class"""

class MyList(list):
    def __init__(self, my_list=None):
        if my_list is None:
            my_list = []
        super().__init__(my_list)

    def print_sorted(self):
        print(sorted(self))
