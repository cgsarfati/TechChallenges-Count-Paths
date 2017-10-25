"""Find total amount of paths from upper left to bottom right of mxn matrix.
    You can only move to the right or down of the cell. Return number
    of paths as an integer via recursion."""

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
    """Recursive sol'n with exponential runtime.

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
    """ Runtime solution of O(mn) r/t nested for loop.

    >>> number_of_paths_optimized(3, 3)
    6

    >>> number_of_paths_optimized(4, 4)
    20

    >>> number_of_paths_optimized(2, 2)
    2
    """

    # initialize matrix to store sum values; start with all 0s
    count = [[0 for x in range(m)] for y in range(n)]

    # count paths for 1st column
    for i in range(m):
        count[i][0] = 1

    # count paths for 1st row
    for j in range(n):
        count[0][j] = 1

    # count paths for other cells by adding left and upper value in matrix
    # fills from top left to bottom right
    for i in range(1, m):
        for j in range(n):
            count[i][j] = count[i-1][j] + count[i][j-1]

    return count[m-1][n-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** All tests passed ***\n"
