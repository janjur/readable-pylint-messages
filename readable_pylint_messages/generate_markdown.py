#!/usr/bin/env python3
""" generate_markdown docstring
This module is complete tool for creating as eyepleasing as possible pylint messages
with error codes and descriptions.
"""
from subprocess import check_output, PIPE
import re
from readable_pylint_messages.Message import Message


def pylint_list_msgs():
    """
    Get every pylint message

    :return: string
    """
    return check_output(['pylint', '--list-msgs'], stderr=PIPE).decode('utf-8')


def prepare_list_of_matches(pattern, text):
    """
    Convert string from pylint to tuples

    :param pattern: regex pattern to compile
    :param text: text to check for msgs
    :return: list of formatted tuples each being msg
    """
    comp = re.compile(pattern)
    matches = re.findall(comp, text)
    new_matches = []
    for match in matches:
        new_matches.append((match[0], match[1], match[2], match[3].strip()))
    return new_matches


def prepare_list_of_messages(matches):
    """
    Converts tuples into Messages

    :param matches: list of formatted tuples each being msg
    :return: list of Messages
    """
    messages = []
    for match in matches:
        message = Message(*match)
        messages.append(message)

    return messages


def main():
    """
    Function handles generating whole README.md

    :return: exit code
    """
    output = pylint_list_msgs()
    matches = prepare_list_of_matches(r":([\w-]+) \((\w+)\): \*([\w \"%]+)\*\n([\w ,\(\)'\n.]+)", output)
    messaeges = prepare_list_of_messages(matches)
    print(messaeges)


if __name__ == '__main__':
    main()
