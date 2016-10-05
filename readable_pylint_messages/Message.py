"""
File implementing Message class
"""


class Message:
    def __init__(self, name, code, brief, description):
        self.name = name
        self.code = code
        self.brief = brief
        self.description = description

    def __repr__(self):
        return "{} {} {} {}\n".format(self.name, self.code, self.brief, self.description)
