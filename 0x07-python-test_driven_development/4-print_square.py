#!/usr/bin/python3
"""defines a name printing function"""


def print_square(size):
    """
    Function to print out the imputed first and last name

    Parameters
    ----------
    size:
        size is the size the square is going to be
    Returns
    --------
    str:
        The # character as a sqaure of whatever inputed size
    Raises
    ----------
    TypeError:
        if size is not an integer
    ValueError:
        if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        print('#' * size)

