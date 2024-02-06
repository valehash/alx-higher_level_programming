#!/usr/bin/python3


"""This module inherits from the list class"""
class MyList(list):
    """class my list that takes sorts a list in ascending order
        parameters
        ----------
        list:
            list to be sorted
    """
    
    def __init__(self, my_list=None):
        if my_list is None:
            my_list = []
        super().__init__(my_list)

    def print_sorted(self):
        """function to print the sorted list
        parameters
        -----------
        self:
            self contains the list to be sorted            

        Returns
        --------
            returns sorted self
        """
        new_list = sorted(self)
        print(new_list)
        
