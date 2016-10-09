#!/usr/bin/env python3
""" generate_markdown docstring
This module is complete tool for creating as eyepleasing as possible pylint messages
with error codes and descriptions.
"""
from shutil import move
from subprocess import check_output, PIPE
from readable_pylint_messages.Message import Message


def pylint_list_msgs():
    """
    Get every pylint message

    :return: string
    """
    return check_output(['pylint', '--list-msgs'], stderr=PIPE).decode('utf-8')


def prepare_list_of_matches(text):
    """
    Convert string from pylint to tuples

    :param pattern: regex pattern to compile
    :param text: text to check for msgs
    :return: list of formatted tuples each being msg
    """
    messages = text[1:].split('\n:')
    new_messages = []

    for message in messages:
        end_of_name = message.find(' ')
        name = message[:end_of_name]
        end_of_code = message.find(')', end_of_name)
        code = message[end_of_name + 2:end_of_code]
        end_of_brief = message.find('\n', end_of_code)
        brief = message[end_of_code + 4:end_of_brief - 1]
        desc = ' '.join([line.strip() for line in message[end_of_brief + 1:].splitlines()])
        new_messages.append((name, code, brief, desc))

    return new_messages


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


def get_pylint_version():
    """
    Get pylint version

    :return: version number string
    """
    output = check_output(['pylint', '--version'], stderr=PIPE).decode('utf-8')
    version = output[7:12]

    return version


def prepare_readme(messages):
    """
    Prepare markdown text

    :param messages: list of Messages
    :return: formatted markdown string
    """
    markdown = "# Readable pylint messages \n"
    markdown += "Prepared with `pylint --list-msgs` for pylint v{}\n".format(get_pylint_version())
    for message in messages:
        markdown += "##{} \n".format(message.name)
        markdown += "####{} - {} \n".format(message.code, message.brief)
        markdown += "{} \n".format(message.description)
    return markdown


def save_to_readme(text):
    """
    Finally, paste generated text to readme

    :param text: string
    :return: None
    """
    with open('README.md', 'w') as readme:
        readme.write(text)
    move('README.md', '../README.md')


def main():
    """
    Function handles generating whole README.md

    :return: exit code
    """
    output = pylint_list_msgs()
    matches = prepare_list_of_matches(output)
    messaeges = prepare_list_of_messages(matches)
    markdown = prepare_readme(messaeges)
    save_to_readme(markdown)


if __name__ == '__main__':
    main()
