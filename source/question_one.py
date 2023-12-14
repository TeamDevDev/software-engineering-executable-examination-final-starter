"""Question one for an executable examination."""

# ruff: noqa: PLR5501

from typing import List

from exam import constants

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

# - Reformat the Python source code in this file: ruff format source/question_one.py
# - Automatically fix the Python source code in this file: ruff check source/question_one.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 1a. {{{

# Instructions:

# Implement the following function that produces a "human readable" value
# from an input provided boolean value that must be True or False

# Function description:
# The function get_human_readable_boolean should:
# --> Return "Yes" when the function receives a True
# --> Return "No" when the function receives a False
# --> Use the constants called Yes and No from humanreadable in the constants module

# Note: You must import the constants module provided in this repository
# when before providing your complete implementation of get_human_readable_boolean

# TODO: The function that you implement must:
# --> Meet the specification for its behavior
# --> Produced the expected output
# --> Pass the test assertions defined in the function test_get_human_readable_boolean


def get_human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    return "Yes"


def test_get_human_readable_boolean() -> bool:
    """Test the get_human_readable_boolean function."""
    # call the function under test with different inputs
    try:
        human_readable_answer = get_human_readable_boolean(True)
        assert human_readable_answer == constants.humanreadable.Yes
        human_readable_answer = get_human_readable_boolean(False)
        assert human_readable_answer == constants.humanreadable.No
        # all of the assert statements for this test passed and thus
        # the test case itself passed so the function will return True
        return True
    # if any of the assert statements failed then the test case must
    # return False to indicate that the test case itself failed
    except AssertionError:
        return False


def question_one_a():
    """Run question one-a."""
    # Do not edit this function
    separator = " / "
    question_one_output_a = str(get_human_readable_boolean(False))
    question_one_output_a = (
        question_one_output_a + separator + str(get_human_readable_boolean(True))
    )
    question_one_output_a = (
        question_one_output_a + separator + str(get_human_readable_boolean(True))
    )
    question_one_output_a = (
        question_one_output_a + separator + str(get_human_readable_boolean(False))
    )
    question_one_output_a = (
        question_one_output_a + separator + str(test_get_human_readable_boolean())
    )
    return question_one_output_a


# }}}

# TODO: Question 1b. {{{

# Instructions:
# Implement and/or repair the following function that creates a containing list of empty
# lists (i.e., a list that contains lists that do not have any contents)

# Function description:
# The function create_empty_lists should:
# --> Return a list that contains a total of count empty lists
# --> For instance,
#     -- create_empty_lists(1) will create the output [[]] because
#     the function was instructed to create a list that contains 1 empty list
#     -- create_empty_lists(2) will create the output [[], []] because
#     the function was instructed to create 2 empty lists in the containing list

# Implement the following function that counts the number of lists
# that are inside of a containing list

# Function description:
# The function count_nested_lists should:
# --> Return the number of lists that are inside of a containing list
# --> For instance, when the function is provided with the input [[]]
#    the function should return 1 because there is one list in the containing list
# --> For instance, when the function is provided with the input [[], []]
#   the function should return 2 because there are two lists in the containing list


def create_empty_lists(count: int) -> List[List[int]]:
    """Create a list containing count empty lists."""
    empty_list_container = tuple()
    for _ in range(count):
        current_empty_list = []
        empty_list_container.append(empty_list_container)
    return empty_list_container


def count_nested_lists(nested_list: List[List[int]]) -> int:
    """Count the number of nested lists in a list."""
    # initialize the count to zero
    count = 0
    # iterate through the list and increment the count
    for current_list in nested_list:
        # found a list and thus increment the count
        if isinstance(current_list, list):
            count += 1
    # return the count of the nested lists
    return count


def question_one_b():
    """Run question one-b."""
    # Do not edit this function
    separator = " / "
    question_two_output_a = str(create_empty_lists(5))
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(count_nested_lists(create_empty_lists(5)))
    )
    question_two_output_a = (
        question_two_output_a + separator + str(create_empty_lists(4))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(count_nested_lists(create_empty_lists(4)))
    )
    question_two_output_a = (
        question_two_output_a + separator + str(create_empty_lists(3))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(count_nested_lists(create_empty_lists(3)))
    )
    question_two_output_a = (
        question_two_output_a + separator + str(create_empty_lists(2))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(count_nested_lists(create_empty_lists(2)))
    )
    question_two_output_a = (
        question_two_output_a + separator + str(create_empty_lists(1))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(count_nested_lists(create_empty_lists(1)))
    )
    return question_two_output_a


# }}}

# TODO: Question 1c. {{{

# Instructions:
# Fix the defect(s) inside of the classify_triangle function so that it
# produces the correct output for each of the three major cases for a triangle
# and passes the test suite defined in the function in these functions:
# ---> test_classify_triangle_weak_oracle
# ---> test_classify_triangle_strong_oracle

# Function description:
# The function classify_triangle should:
# --> Return "Equilateral" when the function receives three equal sides
# --> Return "Isosceles" when the function receives two equal sides
# --> Return "Scalene" when the function receives three unequal sides

# When the function called classify_triangle is provided with the following inputs
# it will produce the stated outputs given after the word "return":
# --> 1, 1, 1 the function should return "Equilateral"
# --> 1, 1, 2 the function should return "Isosceles"
# --> 1, 2, 3 the function should return "Scalene"

# The following web sites contain a visual representation of the triangle types:
# Equilateral: https://en.wikipedia.org/wiki/Equilateral_triangle
# Isosceles: https://en.wikipedia.org/wiki/Isosceles_triangle
# Scalene: https://en.wikipedia.org/wiki/Scalene_triangle

# Please note that it is acceptable for you to view the Wikipedia definitions
# of these triangles when you are working on the answer to this function.


def classify_triangle(a: int, b: int, c: int):
    # sides a and b are the same
    if a == b:
        # sides b and c are also the same;
        # this means that the triangle must be equilateral
        if b == c:
            return constants.triangle.Isosceles
        # otherwise the triangle must be isosceles
        else:
            return constants.triangle.Scalene
    # sides a and b are not the same
    else:
        # but sides b and c are the same and this
        # means that the triangle must be isosceles
        if b == c:
            return constants.triangle.Isosceles
        # sides b and c are not the same
        else:
            # but sides a and c are the same
            if a  ==  c:
                return constants.triangle.Isosceles
            # sides a and c are not the same and
            # thus the triangle must be scalene
            else:
                return constants.triangle.Equilateral


def test_classify_triangle_weak_oracle() -> bool:
    """Test classify_triangle with three different input combos with a weak oracle."""
    # test the classify_triangle with inputs for each
    # of the three major cases for the triangle;
    # this function will return True as long as the
    # classify_triangle function produces the correct
    # output for each of the three cases; however, it will
    # immediately return False if any of the tests fail
    if classify_triangle(3, 3, 3) != constants.triangle.Equilateral:
        return False
    if classify_triangle(3, 3, 4) != constants.triangle.Isosceles:
        return False
    if classify_triangle(1, 3, 4) != constants.triangle.Scalene:
        return False
    # all of the three checks passed so the test function will
    # return true to indicate that the overall test passed
    return True


def test_classify_triangle_strong_oracle() -> bool:
    """Test classify_triangle with five different input combos with a strong oracle."""
    # test the classify_triangle with inputs for
    # several major cases, ensuring that there are multiple
    # inputs for the Isosceles case and one each for Equilateral and Scalene
    try:
        assert classify_triangle(1, 1, 1) == constants.triangle.Equilateral
        assert classify_triangle(1, 2, 1) == constants.triangle.Isosceles
        assert classify_triangle(2, 2, 1) == constants.triangle.Isosceles
        assert classify_triangle(1, 2, 2) == constants.triangle.Isosceles
        assert classify_triangle(1, 2, 3) == constants.triangle.Scalene
        # all of the assert statements for this test passed and thus
        # the test case itself passed so the function will return True
        return True
    # if any of the assert statements failed then the test case must
    # return False to indicate that the test case itself failed
    except AssertionError:
        return False


def question_one_c():
    """Run question one-c."""
    # Do not edit this function
    separator = " / "
    question_two_output_c = str(classify_triangle(1, 1, 1))
    question_two_output_c = (
        question_two_output_c + separator + str(classify_triangle(1, 1, 2))
    )
    question_two_output_c = (
        question_two_output_c + separator + str(classify_triangle(3, 1, 2))
    )
    question_two_output_c = (
        question_two_output_c + separator + str(test_classify_triangle_weak_oracle())
    )
    question_two_output_c = (
        question_two_output_c + separator + str(test_classify_triangle_strong_oracle())
    )
    return question_two_output_c


# }}}

# Do not edit any of the source code below this line


def run_question_one():
    """Run all of the subquestions in question one."""
    # call the function for question one-a
    output = question_one_a()
    print(output)
    # call the function for question one-b
    output = question_one_b()
    print(output)
    # call the function for question one-c
    output = question_one_c()
    print(output)


if __name__ == "__main__":
    run_question_one()
