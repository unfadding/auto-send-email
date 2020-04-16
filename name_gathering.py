from get_email import decoded_email
import email
import re

imported_email_string = decoded_email
email_message = str(imported_email_string)
regex = '(?<=#000000;">)(.*?)(?=<)'
name = re.findall(regex, email_message)

print(name)
