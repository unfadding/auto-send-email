import yagmail
from conf.credentials import email, password
from email_parser import email_list
from body_content import body_content

listed_emails = ['isabellahallite@gmail.com']

print("SENDING E-MAILS...")
for i in range(len(listed_emails)):
    yagmail.SMTP(email, password).send(to=listed_emails[i],
                                       subject='Happy Birthday!',
                                       contents=(body_content))
    print("EMAIL SENT SUCCESSFULY TO:", listed_emails[i])
