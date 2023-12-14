import random
from typing import List, Tuple

# TODO: This file should contain an appropriate docstring for the module

# TODO: All of the functions in this file should have:
# --> A docstring that describes the function's behavior
# --> A type annotation for each of the function's parameters
# --> A type annotation for the function's return value

# TODO: Please adhere to the following guidelines for this file:

# --> Your source code must adhere to industry best practices in, for instance,
# source code formatting, variable naming, and documentation.

# --> To attempt to repair the region(s) where your source code does not adhere
# to industry best practices, you can use your terminal to type these commands
# in the root of the of your GitHub repository:

# - Reformat the Python source code in this file: ruff format source/question_six.py
# - Automatically fix the Python source code in this file: ruff check source/question_six.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 6a. {{{

# Instructions:
# Implement the following function so that it produces output that
# meets the following description

# Function description:
# The function generate_square_matrix should:
# --> Accept as input one int value called size
# --> Generate a square matrix where the number of rows and columns is size
# --> Each of the values in the matrix should be a string representation of
#     a random integer between 0 and 100
# --> Return the matrix as a list of lists of strings

# Note: the function should use the random.randint() function to randomly
# generate the values in the list of lists. Importantly, this approach is
# like the use of a property-based testing framework such as Hypothesis.

# Here is the documentation for the random.randint() function:
# random.randint(a, b):
# Return a random integer N such that a <= N <= b.
# Reference: https://docs.python.org/3/library/random.html


def generate_square_matrix(size: int) -> List[List[str]]:
    """Generate a square matrix where the number of rows and columns is size."""
    matrix: List[List[str]] = []
    return matrix


# Instructions:
# Do not modify the count_rows and count_columns functions
# as they are both used to check the output of the generate_square_matrix function


def count_rows(records: List[List[str]]) -> int:
    """Count the number of rows in a two-dimensional list."""
    return len(records)


def count_columns(records: List[List[str]]) -> int:
    """Count the number of columns in a two-dimensional list."""
    # assume that there are no columns and detect otherwise
    column_count = 0
    # iterate through the rows in the list of lists
    # and then determine the maximum number of columns
    # across all rows inside of the two-dimensional structure
    for row in records:
        # the column count is the maximum number of columns
        # for all of the internal rows of data
        column_count = max(column_count, len(row))
    # return the count of the number of columns
    return column_count


def question_six_a():
    """Run question six-a."""
    # Do not edit this function
    separator = " / "
    question_six_matrix_zero = generate_square_matrix(0)
    question_six_matrix_one = generate_square_matrix(1)
    question_six_matrix_two = generate_square_matrix(2)
    question_six_matrix_three = generate_square_matrix(3)
    return (
        str(
            (
                count_rows(question_six_matrix_zero),
                count_columns(question_six_matrix_zero),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_one),
                count_columns(question_six_matrix_one),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_two),
                count_columns(question_six_matrix_two),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_three),
                count_columns(question_six_matrix_three),
            )
        )
    )


# }}}

# TODO: Question 6b. {{{

# Instructions:
# Implement and/or repair the following function so that it produces output that
# meets the following description

# Function description:
# The function generate_rectangle_matrix should:
# --> Accept as input two int values called num_rows and num_cols
# --> Generate a rectangular matrix where the number of rows is num_rows
#     and the number of columns is num_cols
# --> Each of the values in the matrix should be a string representation of
#     a random integer between 0 and 100
# --> Return the matrix as a list of lists of strings

# Note that the generate_rectangle_matrix function is similar to the
# generate_square_matrix function, except that it generates a rectangular
# matrix instead of a square matrix. If you were to call the generate_rectangle_matrix
# function with the same value for num_rows and num_cols, then it would
# produce the same output as the generate_square_matrix function.


def generate_rectangle_matrix(num_rows: int, num_cols: int) -> List[List[str]]:
    matrix: List[List[int]] =  []
    return matrix


def question_six_b():
    """Run question six-b."""
    # Do not edit this function
    separator = " / "
    question_six_matrix_zero = generate_rectangle_matrix(0, 0)
    question_six_matrix_one = generate_rectangle_matrix(3, 2)
    question_six_matrix_two = generate_rectangle_matrix(2, 3)
    question_six_matrix_three = generate_rectangle_matrix(1, 1)
    return (
        str(
            (
                count_rows(question_six_matrix_zero),
                count_columns(question_six_matrix_zero),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_one),
                count_columns(question_six_matrix_one),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_two),
                count_columns(question_six_matrix_two),
            )
        )
        + separator
        + str(
            (
                count_rows(question_six_matrix_three),
                count_columns(question_six_matrix_three),
            )
        )
    )


# }}}

# TODO: Question 6c. {{{

# Instructions:
# Implement the following function so that it produces output
# according to the following function description

# Function description:
# The function divide_rectangle_matrix_column_counts should:
# --> Accept as input no parameters since it is designed to work in a specific fashion and
#     make its own inputs to two separate calls to the generate_rectangle_matrix function
# --> Generate a rectangle matrix M1 where is column count will be the numerator of a division
# --> Generate a rectangle matrix M2 where is column count will be the denominator of a division
# --> By construction, make sure that the rectangle matrix M2 will have a column count that is zero
# --> Count the number of columns in M1 and M2 and store these in separate int variables
# --> Divide the two column counts and store the result in a float variable
# --> Make sure that the function will throw a ZeroDivisionError since the denominator must be zero
# --> Return a tuple of the two column counts and a boolean flag that indicates if the exception was thrown
# --> Note that the function should be designed in such a fashion that it always
#     throws and subsequently catches the ZeroDivisionError exception and then
#     returns the count of columns in M1, the count of columns in M2, and a boolean flag
#     that will be True to indicate that the ZeroDivisionError exception was thrown;
#     flag should be False to indicate that the exception did not appear


def divide_rectangle_matrix_column_counts():
    # TODO: create inputs for the two calls of the generate_rectangle_matrix
    # function that will ultimately cause this function to throw a
    # ZeroDivisionError, catch the exception, and then return True as the final
    # boolean parameter in the tuple that comprises the return value
    # TODO: count the number of columns in the numerator matrix
    # TODO: count the number of columns in the denominator matrix
    # TODO: implement the remainder of the function so that it produces
    # the correct output according to the function description
    return (0, "0", False)


def test_divide_rectangle_matrix_column_counts() -> bool:
    """Confirm that the determine_relationship function works correctly."""
    # test to confirm that an exception was thrown by the function;
    # note that the first value in this tuple is not explicitly checked
    expected = (10, 0, True)
    actual = divide_rectangle_matrix_column_counts()
    # check the outputs to confirm that the function worked; note that
    # the meaning of "worked" is that it threw the exception, which is
    # indicated by the third value in the tuple which must be True
    if actual[1] != expected[1] and actual[2] != expected[2]:
        return False
    return True


def question_six_c():
    """Run question six-c."""
    # Do not edit this function
    separator = " / "
    question_six_output_c = str(divide_rectangle_matrix_column_counts())
    question_six_output_c = (
        question_six_output_c
        + separator
        + str(test_divide_rectangle_matrix_column_counts())
    )
    return question_six_output_c


# }}}


# Do not edit any of the source code below this line


def run_question_six():
    """Run all of the subquestions in question six."""
    # call the function for question six-a; note
    # that this requires that there is a call_bubble_sort_for_restricted_coverage
    # that must be callable and provided as an input to question_six_a
    output = question_six_a()
    print(output)
    # call the function for question six-b
    output = question_six_b()
    print(output)
    # call the function for question six-c
    output = question_six_c()
    print(output)


if __name__ == "__main__":
    run_question_six()
