"""
19. Write a Python class to find validity of a string of parentheses, '(', ')',
    '{', '}', '[' and ']. These brackets must be close in the correct order, for
    example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid
"""


class Validity():
    valid_dict = {
        "(": ")",
        "{": "}",
        "[": "]"
        }
    temp_list = []

    def __init__(self, some_string):
        self.some_string = some_string

    def is_valid(self):
        for bracket in self.some_string:
            if bracket in self.valid_dict:
                self.temp_list.append(bracket)
            elif len(self.temp_list) == 0 or self.valid_dict[self.temp_list.pop()] != bracket:
                return False
        return len(self.temp_list) == 0


brackets = input("Enter string of brackets: ")
prantheses = Validity(brackets)
result = prantheses.is_valid()
if result:
    print("The parantheses are valid!")
else:
    print("The parantheses are not valid!")
