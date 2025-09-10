def hailstones(n):
    """The hailstones sequence is an integer sequence which follows the
    rule: if the current number is even, then go to half that number;
    else, go to three times that number, plus 1.

    Exercise: implement hailstones(n). At each step, just print out
    the current number on a new line. Two doctests are provided.

    >>> hailstones(8)
    8
    4
    2
    1
    >>> hailstones(3)
    3
    10
    5
    16
    8
    4
    2
    1

    """
    # YOUR CODE HERE
    
import doctest
doctest.testmod(verbose=True, report=True)

