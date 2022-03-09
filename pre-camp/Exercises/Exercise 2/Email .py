
import re

def valid_email_check(input_subject):
    pass
    pattern = "^[\w\.]+@([\w]+\.)+[\w]{2,4}$"
    subject_result = re.match(pattern, input_subject)
    return subject_result


result = (valid_email_check(input()))
if result:
  print("Successful!")
else:
  print("Unsuccessful :(")	