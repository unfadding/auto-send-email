from get_email import decoded_email
import email
import re


def get_email_list_from_body():
    email_message = str(decoded_email)
    regex = r'([\w0-9._-]+@[\w0-9._-]+\.[\w0-9_-]+)'
    emails = re.findall(regex, email_message)
    email_list = emails[29:]
    return email_list, email_message


email_list, email_message = get_email_list_from_body()