def calc_mean(numbers):
    """ Calculate the mean of a list of numbers.

    Arguments:
    numbers -- a list of numbers.

    """
    total = 0
    for num in numbers:
        total = total + num
    return(total / float(len(numbers)))
