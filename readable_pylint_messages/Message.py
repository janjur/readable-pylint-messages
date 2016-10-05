"""
File implementing Message class
"""


class Message:  # pylint: disable=too-few-public-methods
    """
    Class representing pylint error messages
    """
    def __init__(self, name, code, brief, description):
        self.name = name
        self.code = code
        self.brief = brief
        self.description = description
