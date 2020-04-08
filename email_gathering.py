from get_email import decoded_string
import email
import re

imported_email_string = decoded_string
email_message = str(imported_email_string)
regex = r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)'
emails = re.findall(regex, email_message)
print(emails)
#29
