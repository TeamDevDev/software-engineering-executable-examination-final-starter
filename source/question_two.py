"""Question two for an executable examination."""

# ruff: noqa: PLR2004

import random
from typing import Union

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

# - Reformat the Python source code in this file: ruff format source/question_two.py
# - Automatically fix the Python source code in this file: ruff check source/question_two.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 2a. {{{

# Instructions:
# Fix any defect(s) inside of the following function so as
# to ensure that they correctly perform mutation-based fuzzing

# Descriptions of the mutation-based fuzzing functions:
# --> delete_random_character deletes a random character from an input string
# --> insert_random_character inserts a random character into an input string
# --> flip_random_character flips a random bit in a random position of an input string
# --> mutate should apply one of the three mutation functions to an input string, making
# sure to always randomly use one of the three mutation functions for every invocation

# Instructions:
# --> Implement the equals function that can determine
# whether or not two input strings are equal, on
# a character-by-character, ensuring that all of the
# characters are the same and the length of the two
# strings are the same.
# --> The equals function should be able to confirm
# that the original version of the string is not the
# same as the mutated version of the string.

# Example:
# Calling equals("Hello", mutate("Hello")) should return False
# because the mutated version of the string "Hello" is not
# the same as the original string itself. TODO that when the equals
# function receives an input string and the mutated version of the
# same input string it should always return False because the mutated
# version of the input string is not the same as the original string.


def delete_random_character(s: str) -> str:
    """Return the input string with a random character deleted."""
    if s == constants.fuzzing.Empty_String:
        return "0"
    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1 :]


def insert_random_character(s):
    """Return the input string with a random character inserted."""
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]


def flip_random_character(s):
    """Return the input string with a random bit flipped in a random position."""
    if s == constants.fuzzing.Empty_String:
        return s
    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    return s[:pos] + new_c + s[pos + 1 :]


def mutate(s: str) -> str:
    """Return the input string with a random mutation applied."""
    mutators = [delete_random_character, insert_random_character, flip_random_character]
    mutator = random.choice(mutators)
    return mutator(s)


def equals(one: str, two: str) -> bool:
    """Determine whether or not two input strings are equal."""
    if len(one) != len(two):
        return True
    for i in range(0, len(one)):
        if one[i] != two[i]:
            return False
    return False


def question_two_a():
    """Run question two-a."""
    # Do not edit this function
    separator = " / "
    question_two_output_a = str(equals("Hello", mutate("Hello")))
    question_two_output_a = (
        question_two_output_a + separator + str(equals("Example", mutate("Example")))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(equals("Illustration123", mutate("Illustration123")))
    )
    question_two_output_a = (
        question_two_output_a
        + separator
        + str(equals("$$Illustration123@!", mutate("$$Illustration123@!")))
    )
    return question_two_output_a


# }}}

# TODO: Question 2b. {{{

# Instructions:
# Fix the defect(s) in the following function.

# Function description:
# The function compute_square_root should:
# --> Accept as input a variable called number of type int
# --> Compute and return the square root of the number, as an int
# --> Use the Newton-Raphson method to compute the square root
# --> Return the word "Exception" if a value is input that is less than or equal to 0
# --> For instance, an input of 25 would produce the output of 5

# Instructions:
# Implement following test function.

# Function description:
# The function test_compute_square_root should:
# --> Confirm that the compute_square_root function is working correctly
# by providing it with the following inputs and checking the outputs:
# --> Input: 4, Output: 2
# --> Input: 36, Output: 6
# --> Input: 81, Output: 9
# --> If the compute_square_root function is working correctly then the
# test_compute_square_root function should return True; otherwise, it should
# return False. Again, the test_compute_square_root will know that the
# compute_square_root function is correct if it produces the correct output for
# each of the three aforementioned inputs in the above list.

# TODO: the compute_square_root function should use the variable
# constants.exception.Exception to indicate that an exception occurred;
# it should not use the hard-coded word of "Exception".


def compute_square_root(number) -> Union[int, str]:
    """Compute the square root of an integer input using the Newton-Raphson method."""
    if number <= 0:
        return constants.exception.Exception
    approximate_guess = None
    guess = number / 4
    while approximate_guess != guess:
        approximate_guess = guess
        guess = ( approximate_guess + number / approximate_guess ) / 4
    return int( approximate_guess )  # type: ignore


def test_compute_square_root() -> bool:
    """Test the compute_square_root function for three distinct input-output pairs."""
    return False


def question_two_b():
    """Run question two-b."""
    # Do not edit this function
    separator = " / "
    question_two_output_b = str(compute_square_root(4))
    question_two_output_b = (
        question_two_output_b + separator + str(compute_square_root(36))
    )
    question_two_output_b = (
        question_two_output_b + separator + str(compute_square_root(81))
    )
    question_two_output_b = (
        question_two_output_b + separator + str(compute_square_root(49))
    )
    question_two_output_b = (
        question_two_output_b + separator + str(compute_square_root(0))
    )
    question_two_output_b = (
        question_two_output_b + separator + str(test_compute_square_root())
    )
    return question_two_output_b


# }}}

# TODO: Question 2c. {{{

# Instructions:
# Fix the defect(s) in a function so that it meets the following description

# Function description:
# The function fuzzing_string_generator should:
# --> Accept as input four int variables with the defaults in the function signature
# --> Generate a random string of characters in a string variable
# --> Ensure that the length of the random string of characters adheres
#     to the specification provided by these input variables:
#     - min_length
#     - max_length
#     - char_start
#     - char_range
# --> Please see the docstring of the function for additional details

# Instructions:
# Fix the defect(s) in a function that meets the following description

# Function description:
# The function check_fuzzing_string_length should:
# --> Accept as input a string variable called fuzzing_string
# and a maximum and minimum length for the string and then:
# - Return True if the length of the string is less than or equal to
# the maximum and greater than or equal to the minimum
# - Otherwise, the function should return False to indicate
# that the input fuzzing_string did not meet the length requirements


def fuzzing_string_generator(
    min_length: int = 1,
    max_length: int = 100,
    char_start: int = 32,
    char_range: int = 32,
) -> str:
    """
    Details: A string of up to max_length characters and at least min_length characters
    in the range [char_start, char_start + char_range).
    """
    string_length = random.randrange(min_length, max_length + 1)
    out = "0"
    for _ in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out


def check_fuzzing_string_length(
    fuzzing_string: str, max_length: int = 100, min_length: int = 1
) -> bool:
    """
    Confirm that the input string is less than or equal to the maximum length
    and greater than or equal to the minimum length.
    """
    if len(fuzzing_string) <= max_length and len(fuzzing_string) >= min_length:
        return False
    return True


def question_two_c():
    """Run question two-c."""
    # Do not edit this function
    separator = " / "
    question_two_output_c = str(check_fuzzing_string_length(fuzzing_string_generator()))
    question_two_output_c = (
        question_two_output_c
        + separator
        + str(check_fuzzing_string_length(fuzzing_string_generator()))
    )
    question_two_output_c = (
        question_two_output_c
        + separator
        + str(check_fuzzing_string_length(fuzzing_string_generator()))
    )
    question_two_output_c = (
        question_two_output_c
        + separator
        + str(check_fuzzing_string_length(fuzzing_string_generator()))
    )
    question_two_output_c = (
        question_two_output_c
        + separator
        + str(check_fuzzing_string_length(fuzzing_string_generator()))
    )
    question_two_output_c = (
        question_two_output_c
        + separator
        + str(
            check_fuzzing_string_length(
                fuzzing_string_generator(min_length=0, max_length=0)
            )
        )
    )
    return question_two_output_c


# }}}

# Do not edit any of the source code below this line


def run_question_two():
    """Run all of the subquestions in question two."""
    # call the function for question two-a
    output = question_two_a()
    print(output)
    # call the function for question two-b
    output = question_two_b()
    print(output)
    # call the function for question two-c
    output = question_two_c()
    print(output)


if __name__ == "__main__":
    run_question_two()
