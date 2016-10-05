#!/usr/bin/env python3
""" generate_markdown docstring
This module is complete tool for creating as eyepleasing as possible pylint messages
with error codes and descriptions.
"""
from subprocess import check_output, PIPE
from re import compile, findall


def pylint_list_msgs():
    return check_output(['pylint', '--list-msgs'], stderr=PIPE).decode('utf-8')


def prepare_list_of_matches(pattern, text):
    comp = compile(pattern)
    matches = findall(comp, text)
    new_matches = []
    for match in matches:
        new_matches.append((match[0], match[1], match[2], match[3].strip()))
    return new_matches


def main():
    """
    Function handles generating whole README.md

    :return: exit code
    """
    msgs = pylint_list_msgs()
    list_of_msgs = prepare_list_of_matches(r":([\w-]+) \((\w+)\): \*([\w \"%]+)\*\n([\w ,\(\)'\n.]+)", msgs)
    print(list_of_msgs)

if __name__ == '__main__':
    main()
