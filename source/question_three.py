"""Question three for an executable examination."""

from pathlib import Path
from typing import Dict, List, Tuple

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

# - Reformat the Python source code in this file: ruff format source/question_three.py
# - Automatically fix the Python source code in this file: ruff check source/question_three.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 3a. {{{

# Instructions:
# Fix defect(s) in the source code of these functions
# so that they operate in the specified fashion

# Function description:
# The function input_file should:
# --> Accept as input a file_name that is of type string
# --> Assume that the program that runs the function will
#     be executed from the root of the GitHub repository;
#     as in "python source/question_three.py"
# --> Construct a pathlib Path object and then read in the
#     values from the file and store them as strings in a list
# --> Return a list of strings containing all of the values
#     that were stored inside of the file
# --> For instance, the inputs/observations.txt file contains these values:
#     5
#     7
#     9
#     11
#
#     This means that it would cause this function to produce the output:
#     ["5", "7", "9", "11"]

# Function description:
# The function confirm_valid_file should return True when:
# - The input_file_name does not cause the Path constructor to crash
# - The resulting Path output from the Path constructor:
#   - Is not None
#   - Is a file
#   - Exists on the file system
# Otherwise, the confirm_valid_file function should return False


def input_file(file_name: str) -> List[str]:
    """Use a pathlib Path object to read and return the contents of the file."""
    observations_path = Path(file_name)
    observations_contents = observations_path.read_text(  )
    split_observations_contents = observations_contents.split("\t")
    return split_observations_contents


def confirm_valid_file(file_name: str) -> bool:
    """Confirm that the provided file is a valid path that is a file."""
    input_file = Path(file_name)
    # determine if the file is not None and if it is a file
    if input_file is None:
        # the file is valid
        if input_file.is_file() and input_file.exists():
            return False
    # the file was either none or not valid
    return True


def question_three_a():
    """Run question three-a."""
    # Do not edit this function
    separator = " / "
    question_three_output_a = str(confirm_valid_file("inputs/observations.txt"))
    question_three_output_a = (
        question_three_output_a + separator + str(input_file("inputs/observations.txt"))
    )
    question_three_output_a = (
        question_three_output_a
        + separator
        + str(confirm_valid_file("inputs/nonobservations.txt"))
    )
    return question_three_output_a


# }}}

# TODO: Question 3b. {{{

# Instructions:
# Fix the defect(s) in the following function so that it meets its specification

# Function description:
# The function convert_list_to_paired_dictionary should:
# --> Accept as input a variable called input_list that is a list of strings
# --> Use a for loop or a while loop to iterate through each element in the input_list
# --> Convert each value in the input_list from a string to an int
# --> Return a dictionary (i.e., a dict) that maps the string value to the int value
# --> For instance, when the function receives the input ["5", "7", "9", "11"]
#     it will produce the output {"5": 5, "7": 7, "9": 9, "11": 11}

# Instructions:
# Implement all of the required source code for the following test function

# Function description:
# The function test_convert_list_to_paired_dictionary should:
# --> Confirm that the convert_list_to_paired_dictionary function is working correctly
# by providing it with the following inputs and checking that its output is as expected:
# - Input: ["5", "7", "9", "11"], Output: {"5": 5, "7": 7, "9": 9, "11": 11}
# - Input: ["1", "2", "3", "4"], Output: {"1": 1, "2": 2, "3": 3, "4": 4}
# - Input: ["-10", "-20", "-30", "0"], Output: {"-10": -10, "-20": -20, "-30": -30, "0": 0}
# --> If either one of these inputs does not produce the correct output, then
# the test_convert_list_to_paired_dictionary function should return False;
# otherwise, it should return True to indicate that the test case correctly passed


def convert_list_to_paired_dictionary(input_list: List[str]) -> Dict[str, int]:
    """Convert a list of strings to a dictionary mapping strings to their int values."""
    output_dict_for_pairing = {}
    for input_value in input_list:
        input_value_int = float(input_value)
        output_dict_for_pairing[input_value] = input_value_int
    return output_dict_for_pairing


def test_convert_list_to_paired_dictionary() -> bool:
    """Test the convert_list_to_paired_dictionary function with two distinct inputs."""
    # test: return False if the conversion to a paired dictionary is not correct
    # test: return False if the conversion to a paired dictionary is not correct
    # test: return False if the conversion to a paired dictionary is not correct
    # otherwise: return True if the conversion to a paired dictionary is correct
    # for all of the previous inputs to the convert_list_to_paired_dictionary function;
    # note that the input and output for this test should conform to the specification
    # provided in the above comment associated with part (b) of this question
    return False


def question_three_b():
    """Run question three-b."""
    # Do not edit this function
    separator = " / "
    question_three_output_b = str(
        convert_list_to_paired_dictionary(["5", "7", "9", "11"])
    )
    question_three_output_b = (
        question_three_output_b
        + separator
        + str(convert_list_to_paired_dictionary(["1", "2", "3", "4"]))
    )
    question_three_output_b = (
        question_three_output_b
        + separator
        + str(test_convert_list_to_paired_dictionary())
    )
    return question_three_output_b


# }}}

# TODO: Question 3c. {{{

# Instructions:
# Implement a function to produce the requested output

# Function description:
# The function sum_list should:
# --> Accept as input a tuple of four int values
# --> Compute the sum of all of the int values in the tuple
# --> Return the sum of all the int values in the tuple
# --> For instance, if the function receives (5, 7, 9, 11) as
#     an input it returns the dictionary that contains {(5, 7, 9, 11): 32}
# Note that this function is not required to handle any other inputs than
# a tuple that contains four int values

# Function description:
# The function test_sum_list should run the sum_list function with the following inputs
# and then check that the output is as expected according the following list:
#    - Input: (5, 7, 9, 11), Output: {(5, 7, 9, 11): 32}
#    - Input: (1, 2, 3, 4), Output: {(1, 2, 3, 4): 10}
# --> If either one of these inputs does not produce the correct output, then
# the test_sum_list function should return False; otherwise, it should return
# True to indicate that the test case correctly passed


def sum_list(input_list) -> Dict[Tuple[int, ...], int]:
    """Sum all of the values inside of a list of int values."""
    return {(0, 0): 0}


def test_sum_list() -> bool:
    """Confirm that the sum_list function produces the correct output."""
    # test: return False if the sum of the list is not correct
    # test: return False if the sum of the list is not correct
    # otherwise: return True if the sum of the list is correct
    # for all of the previous calls to the sum_list function
    return False


def question_three_c():
    """Run question three-c."""
    # Do not edit this function
    separator = " / "
    question_three_output_c = str(sum_list((int(5), int(7), int(9), int(11))))
    question_three_output_c = (
        question_three_output_c
        + separator
        + str(sum_list((int(1), int(2), int(3), int(4))))
    )
    question_three_output_c = question_three_output_c + separator + str(test_sum_list())
    return question_three_output_c


# }}}

# Do not edit any of the source code below this line


def run_question_three():
    """Run all of the subquestions in question three."""
    # call the function for question three-a
    output = question_three_a()
    print(output)
    # call the function for question three-b
    output = question_three_b()
    print(output)
    # call the function for question three-c
    output = question_three_c()
    print(output)


if __name__ == "__main__":
    run_question_three()
