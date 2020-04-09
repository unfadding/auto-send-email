import yagmail
from email_gathering import email_list

try:
    yagmail.SMTP('isabella.hallite@globant.com', 'ymkwtkxzfprcnjnf').send(
        to='isabellahallite@gmail.com',
        subject='Happy Birthday!',
        contents=yagmail.inline('birthday card.png'))
    #contents=yagmail.inline('birthday card.png'))
    print("Email sent successfully")

except:
    print("Error, email was not sent")
