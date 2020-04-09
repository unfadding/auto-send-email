from get_email import decoded_string
import email
import re

imported_email_string = decoded_string
email_message = str(imported_email_string)
regex = '(?<=#000000;">)(.*?)(?=<)'
name = re.findall(regex, email_message)

print(name)
