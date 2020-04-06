import imaplib
import quopri

FROM_EMAIL = "isabella.hallite@globant.com"
FROM_PWD = "dzdtjaftnhvdnpwk"
SMTP_SERVER = "imap.gmail.com"  # padrão
SMTP_PORT = 993  # padrão

# Abrimos a conexão com o servidor e efetuamos o login.
mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL, FROM_PWD)

# Neste ponto selecionamos a caixa de e-mail que queremos fazer a leitura, no meu caso, utilizei “inbox” para leitura dos e-mails. Como também vamos atribuir um label aos e-mails “processados”, passamos o parâmetro readonly=False
mail.select('inbox', readonly=False)

type_mail, data = mail.search(None, 'SUBJECT Birthdays!')

mail_id = data[0]

id_list = mail_id.split()

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)')
    raw_email = data[0][1]

raw_email_string = raw_email.decode('utf-8')

decoded_string = quopri.decodestring(raw_email_string)
