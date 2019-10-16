#!/usr/bin/python3


class MyList(list):
    """Represent a list that inherits from a built-in list."""
    def print_sorted(self):
        """Print a list that sorted in ascending order."""
        copy_list = self[:]
        copy_list.sort()
        print(copy_list)

