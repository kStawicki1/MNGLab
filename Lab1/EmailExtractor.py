import re

class EmailExtractor:



    def __init__(self, email):
        self.email = email
        self.regex = "(?P<name>^[a-z]+)\.(?P<surname>[a-z]+)([0-9]+)?@(?P<student>student)?(\.)?wat.edu.pl"

    def is_student(self):
        return re.search(self.regex, self.email).group(4) == "student"

    def get_name(self):
        return re.search(self.regex, self.email).group(1).capitalize()

    def get_surname(self):
        return re.search(self.regex, self.email).group(2).capitalize()

    def is_male(self):
        name = re.search(self.regex, self.email).group(1)
        return name[len(name) - 1] != 'a'
