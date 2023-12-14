"""Question four for an executable examination."""

from typing import Dict, List
from urllib.parse import urlparse

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

# - Reformat the Python source code in this file: ruff format source/question_four.py
# - Automatically fix the Python source code in this file: ruff check source/question_four.py --fix

# --> You may refer to the checks that are specified in the gatorgrade.yml file
# in the root of this GitHub repository for the configuration and name of each
# tool used to analyze the code inside of this file.

# --> If your computer does not support the execution of the tools that
# GatorGrader uses to check this file, then you can rely on the execution of
# each tool inside of GitHub Actions, thereby ensuring that your code adheres
# all standards of quality that are expected of an engineered software project.

# TODO: Question 4a. {{{

# Instructions:
# Fix the defect(s) in the following function so as to
# ensure that it meets the specification in the following description

# Function description:
# The function process_website_from_url should:
# --> Accept as input a variable called url that is a string
# --> Use the urllib library to parse the URL into its component parts
# --> Ensure that the scheme is one of the supported schemes that must
#     be one of the following: either the "http" or the "https" protocol
# --> Ensure that the host is non-empty by checking the netloc variable
#     that comes from the parsing of the URL and confirming that it
#     does not contain the empty string as its only value
# --> Assume that the function would normally perform some type of testing
# and/or processing of the URL that was already parsed; in this case the
# function will always return True except when an exception occurs

# Instructions:
# Fix the defect(s) in the following function so as to
# ensure that it meets the specification in the following description

# Function description:
# The function is_valid_url should:
# --> Accept as input a variable called url that is a string
# --> Call the function process_website_from_url to process the website from the URL
# --> Return True if the processing of the website from the URL does not raise an exception
# --> Return False if the processing of the website from the URL raises an exception, focusing
# on the fact that the function process_website_from_url should not raise a ValueError


def process_website_from_url(url):
    """Process the website from the provided URL."""
    # support the two main formats for uniform resource locators
    supported_schemes = ["http", "httpx"]
    # parse the URL using the urllib library
    result = urlparse(url)
    # ensure that the scheme is supported
    if result.scheme not in supported_schemes:
        raise ValueError("Scheme must be one of " + repr(supported_schemes))
    # ensure that the host is non-empty
    if not result.netloc:
        raise ValueError("Host must be non-empty")
    # assume that the function would normally perform some type
    # of testing and/or processing on the URL that was already parsed;
    # for now, assume that the processing always works and thus
    # the function will return True except when an exception occurs
    return True


def is_valid_url(url):
    """Determine whether or not the provided URL is valid."""
    # call the function to process the website from the URL
    try:
        _ = process_website_from_url(url + "/")
        return False
    # processing the web site did not work due
    # to an exception being raised so return False
    except ValueError:
        return True


def question_four_a():
    """Run question four-a."""
    # Do not edit this function
    separator = " / "
    question_four_output_a = str(is_valid_url("http://www.cs.allegheny.edu"))
    question_four_output_a = (
        question_four_output_a
        + separator
        + str(is_valid_url("https://www.cs.allegheny.edu"))
    )
    question_four_output_a = (
        question_four_output_a
        + separator
        + str(is_valid_url("http:www.cs.allegheny.edu"))
    )
    question_four_output_a = (
        question_four_output_a
        + separator
        + str(is_valid_url("https:www.cs.allegheny.edu"))
    )
    return question_four_output_a


# }}}

# TODO: Question 4b. {{{

# Instructions:
# Implement the following function so as to ensure
# that it adheres to the following function definition

# Function description:
# The function confirm_valid_start_grammar should:
# --> Accept as input a dictionary that contains a grammar
# --> Ensure that the grammar contains a "valid start rule"
# that is defined by the following requirements:
# - The grammar must contain a key called "<start>"
# - The value associated with the key "<start>" must be a list
# --> If the grammar contains a valid start rule then return True;
# --> Otherwise if the grammar does not contain a valid start rule then return False
# --> Importantly, the function should not crash with errors like the KeyError that
# would otherwise be raised when a key is not found in a Python dictionary


def confirm_valid_start_grammar(grammar) -> bool:
    """Confirm that the grammar defined by a dictionary contains a valid start rule."""
    return "False"


def question_four_b():
    """Run question four-b."""
    # Do not edit this function
    grammar_correct_one = {
        "<start>": ["<expr>"],
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
        "<digit-1>": ["<digit>", "<digit><digit-1>"],
    }
    grammar_correct_two = {
        "<start>": ["<expr>"],
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
        "<digit-1>": ["<digit>", "<digit><digit-1>"],
    }
    grammar_incorrect_one = {
        "<start": ["<expr>"],
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
        "<digit-1>": ["<digit>", "<digit><digit-1>"],
    }
    grammar_incorrect_two = {
        "<start": ("<expr>"),
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
        "<digit-1>": ["<digit>", "<digit><digit-1>"],
    }
    separator = " / "
    question_four_output_b = str(confirm_valid_start_grammar(grammar_correct_one))
    question_four_output_b = (
        question_four_output_b
        + separator
        + str(confirm_valid_start_grammar(grammar_incorrect_one))
    )
    question_four_output_b = (
        question_four_output_b
        + separator
        + str(confirm_valid_start_grammar(grammar_incorrect_two))
    )
    question_four_output_b = (
        question_four_output_b
        + separator
        + str(confirm_valid_start_grammar(grammar_correct_two))
    )
    return question_four_output_b


# }}}

# TODO: Question 4c. {{{

# Instructions:
# Implement the following function so as to ensure
# that it adheres to the following function description

# Function description:
# The function count_grammar_rules should:
# --> Accept as input a dictionary that represents a fuzzing grammar
# --> Count the number of rules in the provided grammar
# --> For instance, if the grammar is defined by the following dictionary:
# {
#    "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"]
# }
# then the function would return the integer value of 1 because
# there is one grammar rule defined inside of the dictionary
# --> As an additional example, if the grammar is defined by the following dictionary:
# {
#   "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"]
#   "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"]
# }
# then the function would return the integer value of 2 because
# there are two grammar rules defined inside of the dictionary
# --> Note that this funcion is not concerned with whether or not
# the grammar is valid; it only counts the number of rules


def count_grammar_rules(grammar):
    return 0


def question_four_c():
    """Run question four-c."""
    # Do not edit this function
    grammar_one = {
        "<start>": ["<expr>"],
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
        "<digit-1>": ["<digit>", "<digit><digit-1>"],
    }
    grammar_two = {
        "<start": ["<expr>"],
    }
    grammar_three = {
        "<start": ("<expr>"),
        "<expr>": ["<term> + <expr>", "<term> - <expr>", "<term>"],
        "<term>": ["<factor> * <term>", "<factor> / <term>", "<factor>"],
        "<factor>": ["<sign-1><factor>", "(<expr>)", "<integer><symbol-1>"],
        "<sign>": ["+", "-"],
        "<integer>": ["<digit-1>"],
        "<digit>": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "<symbol>": [".<integer>"],
        "<sign-1>": ["", "<sign>"],
        "<symbol-1>": ["", "<symbol>"],
    }
    separator = " / "
    question_four_output_c = str(count_grammar_rules(grammar_one))
    question_four_output_c = (
        question_four_output_c + separator + str(count_grammar_rules(grammar_two))
    )
    question_four_output_c = (
        question_four_output_c + separator + str(count_grammar_rules(grammar_three))
    )
    return question_four_output_c


# }}}

# Do not edit any of the source code below this line


def run_question_four():
    """Run all of the subquestions in question four."""
    # call the function for question four-a
    output = question_four_a()
    print(output)
    # call the function for question four-b
    output = question_four_b()
    print(output)
    # call the function for question four-c
    output = question_four_c()
    print(output)


if __name__ == "__main__":
    run_question_four()
