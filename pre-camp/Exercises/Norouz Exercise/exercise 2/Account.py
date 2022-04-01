import re, hashlib
from unittest import result
import Site

class Account:
    def __init__(self, username, password, phone_number, email):
        
        pattern = "[a-z A-Z]+_+[a-z A-Z]"
        if re.match(pattern, username):
            self.username = username
        else:
            raise Exception("invalid username")

        pattern = ""
        if re.match(pattern, password):
            self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        else:
            raise Exception("invalid password")

        pattern1 = "^09\d{9}$"
        pattern2 = "^\+989\d{9}$"
        if re.match(pattern1, phone_number):
            self.phone_number = phone_number
        elif re.match(pattern2, phone_number):
            self.phone_number = "0" + phone_number[2:]
        else:
            raise Exception("invalid phone number")

        pattern = "^([\w\.\_\-]+)@([\w\-\_]+)((\.([A-Za-z]){2,5})+)$"
        if re.match(pattern, email):
            self.email = email
        else:
            raise Exception("invalid email")
    @staticmethod
    def log_in(password, username=None, email=None):
        if username != None and email != None and password != None:
            return ({"password": password, "username": username, "email": email})

        elif password != None and username != None and email == None:
            if "@" in username:
                email = username
                return ({"password": password, "email": email})
            else:
                return ({"password": password, "username": username})
