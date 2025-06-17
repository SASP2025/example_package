import numpy


def add_five(input_number):
    """ Take the input values and add 5 to it.


    Parameters
    ----------

    input_number: number
        The input value, should be an integer or float

    Returns
    -------
    The input value with 5 added to it
    """
    if not isinstance(input_number,  (int,float)):
        raise ValueError("input value must be an int or float")
    else:
        return input_number + 5


