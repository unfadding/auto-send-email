import yagmail
from email_gathering import email_list
import keyring

listed_emails = ['isabellahallite@gmail.com']

try:
    yagmail.SMTP('isabella.hallite@globant.com',
                 keyring.get_password("system", "isabella.hallite")).send(
                     to=listed_emails,
                     subject='Happy Birthday!',
                     contents=yagmail.inline('birthday card.png'))
    print("Email sent successfully to", listed_emails)

except:
    print("Error, email was not sent")
