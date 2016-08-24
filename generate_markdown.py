#!/usr/bin/env python3
from subprocess import check_output, PIPE


def main():
    pylint_messages = check_output(['pylint', '--list-msgs'], stderr=PIPE)
    print(pylint_messages.decode('utf-8'))

if __name__ == '__main__':
    main()
