from get_email import decoded_email
import email
import re

imported_email_string = decoded_email
email_message = str(imported_email_string)
regex = r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)'
emails = re.findall(regex, email_message)
email_list = emails[29:]