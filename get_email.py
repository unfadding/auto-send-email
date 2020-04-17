import imaplib
import quopri
from conf.credentials import email, password, server
from todays_email import todays_email


def get_todays_email():
    print('GETTING E-MAIL FROM SERVER...')
    mail = imaplib.IMAP4_SSL(server)
    mail.login(email, password)
    mail.select('inbox')
    type_mail, email_id = mail.search(None, todays_email)
    print('OK. GOT {}'.format(todays_email))
    return type_mail, email_id, mail


def get_email_content():
    typ, email_data = mail.fetch(email_id[0], '(RFC822)')
    raw_email = email_data[0][1]
    return raw_email


def decode_email():
    raw_email_string = raw_email.decode("utf-8")
    decoded_email = quopri.decodestring(raw_email_string)
    print('E-MAIL SUCCESSFULY IMPORTED')
    return decoded_email


type_mail, email_id, mail = get_todays_email()
raw_email = get_email_content()
decoded_email = decode_email()