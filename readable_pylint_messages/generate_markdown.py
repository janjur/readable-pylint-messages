""" generate_markdown docstring
This module is complete tool for creating as eyepleasing as possible pylint messages
with error codes and descriptions.
"""

from subprocess import check_output, PIPE


def main():
    """
    Function handles generating whole README.md

    :return: exit code
    """
    pylint_messages = check_output(['pylint', '--list-msgs'], stderr=PIPE)
    print(pylint_messages.decode('utf-8'))

if __name__ == '__main__':
    main()
