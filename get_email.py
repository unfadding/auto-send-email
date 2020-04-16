import imaplib
import quopri
from conf.credentials import email, password, server


def get_last_email():
    mail = imaplib.IMAP4_SSL(server)
    mail.login(email, password)
    mail.select('inbox')
    type_mail, email_id = mail.search(None, 'SUBJECT Birthdays!')
    return type_mail, email_id, mail


type_mail, email_id, mail = get_last_email()


def get_email_content():
    typ, email_data = mail.fetch(email_id[0], '(RFC822)')
    raw_email = email_data[0][1]
    return raw_email


raw_email = get_email_content()


def decode_email():
    raw_email_string = raw_email.decode("utf-8")
    decoded_email = quopri.decodestring(raw_email_string)
    return decoded_email


decoded_email = decode_email()