# SOLUTION
# 3x3 matrix

# Starting from top left, traversing on sides is only 1 move
# [ ? ? ? ] --> [ 1 1 1 ]
# [ ? ? ? ] --> [ 1 ? ? ]
# [ ? ? ? ] --> [ 1 ? ? ]

# To figure out num paths of rest, add left and upper num together
# [ 1 1 1 ] --> [ 1 1 1 ]
# [ 1 ? ? ] --> [ 1 2 3 ]
# [ 1 ? ? ] --> [ 1 3 6 ] --> 6


def number_of_paths_recursion(m, n):
    """Find total amount of paths from upper left to bottom right of mxn matrix.
    You can only move to the right or down of the cell. Return number
    of paths as an integer via recursion.

    >>> number_of_paths_recursion(3, 3)
    6

    >>> number_of_paths_recursion(4, 4)
    20

    >>> number_of_paths_recursion(2, 2)
    2
    """

    # BASE CASE: if row or col num is 1, stop recursing
        # also fast-out (if initial value is only a column or a row)
    if (m == 1 or n == 1):
        return 1

    return number_of_paths_recursion(m-1, n) + number_of_paths_recursion(m, n-1)


def number_of_paths_optimized(m, n):
    """ Runtime solution of O(mn).

    >>> number_of_paths_optimized(3, 3)
    6

    >>> number_of_paths_optimized(4, 4)
    20

    >>> number_of_paths_optimized(2, 2)
    2
    """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** All tests passed ***\n"
