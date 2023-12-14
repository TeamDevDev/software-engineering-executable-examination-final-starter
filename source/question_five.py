"""Question five for an executable examination."""

import sys
from typing import Callable, List, Tuple

from exam.debug import DebugLevel

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

# - Reformat the Python source code in this file: ruff format source/question_five.py
# - Automatically fix the Python source code in this file: ruff check source/question_five.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 5a. {{{

# Instructions:

# --> Correctly define the variables input_one and input_two so that
# the function called call_bubble_sort_for_restricted_coverage
# will only cause seven distinct lines of the source code for the
# bubble_sort function to be reported as executed during test coverage monitoring

# The function call_bubble_sort_for_restricted_coverage should:
# --> Define lists called input_one and input_two that will ensure
# that the only lines of the code for part (a) that are covered
# are those that are marked with the comment label "--> run"
# --> Specifically, the two lists should ultimately cause
# seven distinct lines of source code to be reported as executed
# by the test coverage monitor defined in the trace_lines function

# Important reminders about some of the functions for this question part:
# --> Do not change the implementation of the bubble_sort function
# --> Do not change the implementation of the trace_lines function
# --> Define the input_one and input_two lists so that they are
# declared on exactly the lines that are marked with the comment "--> run"

# declare a global variable that will store a
# list of the lines that were executed by the
# bubble sort function when coverage monitoring
# through the sys.settrace function is enabled;
# the value of the executed_lines variable should
# be an empty list before the trace_lines function is called
executed_lines = []


def trace_lines(frame, event, _):
    """Trace the execution of the program, recording the lines that are executed."""
    # do not change the implementation of this function as doing
    # so may cause other parts of this question to not work correctly
    if event == "line":
        executed_lines.append(frame.f_lineno)
    return trace_lines


def bubble_sort(list_one, list_two):
    """Perform a bubble sort of the joined version of the input lists."""
    # do not change the implementation of this function as doing
    # so may cause other parts of this question to not work correctly
    combined_list = list_one + list_two  # --> run
    list_length = len(combined_list)  # --> run
    for i in range(list_length):  # --> run
        for j in range(0, list_length - i - 1):
            if combined_list[j] > combined_list[j + 1]:
                combined_list[j], combined_list[j + 1] = (
                    combined_list[j + 1],
                    combined_list[j],
                )
    return combined_list  # --> run


def call_bubble_sort_for_restricted_coverage():
    """Call the bubble sort function in a way that yields restricted test coverage."""
    # define the first input to the bubble sort function;
    # do not delete this line; make sure that you define a list
    # for input_one that will meet the criteria for this question
    input_one = [0, 1, 2, 3]  # --> run
    # define the second input to the bubble sort function;
    # do not delete this line; make sure that you define a list
    # for input_two that will meet the criteria for this question
    input_two = [9, 10, 11, 0, 1]  # --> run
    _ = bubble_sort(input_one, input_two)  # --> run


def question_five_a(bubble_sort_function: Callable):
    """Run question five-a."""
    # Do not edit this function
    sys.settrace(trace_lines)
    bubble_sort_function()
    sys.settrace(None)
    # return the number of lines
    return len(executed_lines)


# }}}

# TODO: Question 5b. {{{

# Instructions:
# Implement the logging function so that it operates according this description

# The function called log should:
# --> Accept as input one string called message
# --> Accept as input a variable called debug_level that is of type DebugLevel
# --> Prepend the stated debugging level inside of brackets to the provided message
# --> For instance, if the function call is:
#       -- log("Opened the file", debug_level=DebugLevel.INFO)
#     this would produce the following output:
#       -- "[INFO] Opened the file" as a string
# --> If the debug_level variable does not match one of the valid
# values for the DebugLevel then it should return an empty string
# --> Note that this function must use the logging levels specified as
# constants in the DebugLevel class found in the debug module; this
# means that you will need to write the correct import for this to work


def log(message: str, debug_level=DebugLevel.INFO) -> str:
    """Produce logging output at the specified level of debugging."""
    return  0


def question_five_b():
    """Run question five-b."""
    # Do not edit this function
    separator = " / "
    question_five_output_b = log("Opened the file", debug_level=DebugLevel.INFO)
    question_five_output_b = (
        question_five_output_b
        + separator
        + log("Executed dangerous if statement", debug_level=DebugLevel.WARNING)
    )
    question_five_output_b = (
        question_five_output_b
        + separator
        + log("Unresolved network error", debug_level=DebugLevel.CRITICAL)
    )
    return question_five_output_b


# }}}

# Question 5c. {{{

# Instructions:
# Implement the following function so that it produces output
# according to the following function description

# Function description:
# The function determine_relationship should:
# --> Accept as input two int values called input_one and input_two
# --> If the value in input_one is less than input_two
#     then the function should return a tuple containing (input_one, input_two, "<")
# --> If the value in input_one is greater than input_two
#     then the function should return a tuple containing (input_one, input_two, ">")
# --> If the value in input_one is exactly equal to input_two
#     then the function should return a tuple containing (input_one, input_two, "=")

# Instructions:
# Implement the following test function so that it produces output
# according to the following function description

# Function description:
# The function test_determine_relationship should confirm that when
# the determine_relationship function is provided with the following input it
# will produce the specified output:
# --> Input one = 12, Input two = 10 produces the output (12, 10, '>')
# --> Input one = 10, Input two = 12 produces the output (10, 12, '<')
# --> Input one = 10, Input two = 10 produces the output (10, 10, '=')
# When the determine_relationship function produces the correct output for
# each of the three aforementioned inputs then it should return True;
# otherwise, the test_determine_relationship function should return False


def determine_relationship(input_one: int, input_two: int) -> Tuple[int, int, str]:
    """Determine the numerical relationship between the two input values."""
    if input_one < input_two:
        return (input_one, input_two, "<")
    elif input_one > input_two:
        return (input_one, input_two, ">")
    else:
        return (input_one, input_two, "=")


def test_determine_relationship() -> bool:
    """Confirm that the determine_relationship function works correctly."""
    # test case one
    input_one = 12
    input_two = 10
    expected = (12, 10, ">")
    actual = determine_relationship(input_one, input_two)
    if actual != expected:
        return False
    # test case two
    input_one = 10
    input_two = 12
    expected = (10, 12, "<")
    actual = determine_relationship(input_one, input_two)
    if actual != expected:
        return False
    # test case three
    input_one = 10
    input_two = 10
    expected = (10, 10, "=")
    actual = determine_relationship(input_one, input_two)
    if actual != expected:
        return False
    return True


def question_five_c():
    """Run question five-c."""
    # Do not edit this function
    separator = " / "
    question_five_output_b = str(determine_relationship(12, 10))
    question_five_output_b = (
        question_five_output_b + separator + str(determine_relationship(3, 9))
    )
    question_five_output_b = (
        question_five_output_b + separator + str(determine_relationship(2, 2))
    )
    question_five_output_b = (
        question_five_output_b + separator + str(test_determine_relationship())
    )
    return question_five_output_b


# }}}


# Do not edit any of the source code below this line


def run_question_five():
    """Run all of the subquestions in question five."""
    # call the function for question five-a; note
    # that this requires that there is a call_bubble_sort_for_restricted_coverage
    # that must be callable and provided as an input to question_five_a
    output = question_five_a(call_bubble_sort_for_restricted_coverage)
    print(output)
    # call the function for question five-b
    output = question_five_b()
    print(output)
    # call the function for question five-c
    output = question_five_c()
    print(output)


if __name__ == "__main__":
    run_question_five()
