import yagmail
yag = yagmail.SMTP()
contents = ['Teste']
yag.send('isabella.hallite@globant.com', 'subject', contents)