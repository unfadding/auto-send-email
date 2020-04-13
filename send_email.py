import yagmail
from email_gathering import email_list
import keyring

listed_emails = ['']

for i in range(len(listed_emails)):
    yagmail.SMTP('isabella.hallite@globant.com',
                 keyring.get_password("system", "isabella.hallite")).send(
                     to=listed_emails[i],
                     subject='Happy Birthday!',
                     contents=yagmail.inline('birthday card.png'))
    print("Email sent successfully to", listed_emails[i])
