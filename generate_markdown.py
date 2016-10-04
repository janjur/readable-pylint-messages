#!/usr/bin/env python3
from subprocess import check_output, PIPE

def pylint_list_msgs():
	return check_output(['pylint', '--list-msgs'], stderr=PIPE).decode('utf-8')

def main():
    print(pylint_list_msgs())

if __name__ == '__main__':
    main()
