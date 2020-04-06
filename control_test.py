import imaplib, email, os

user = 'isabella.hallite@globant.com'
password = ''
imap_url = 'imap.gmail.com'


# sets up the auth
def auth(user, password, imap_url):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    return con


# extracts the body from the email
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


#search for a particular email
def search(key, value, con):
    result, data = con.search(None, 'SUBJECT Birthdays!')
    return data


#extracts emails from byte array
def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs


con = auth(user, password, imap_url)
con.select('INBOX')

result, data = con.fetch(b'10', '(RFC822)')
raw = email.message_from_bytes(data[0][1])
print(get_body(raw))