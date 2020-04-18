from get_email import email_id, mail
from todays_email import todays_email


def copy_todays_email_to_newfolder():
    print('COPYING:', email_id[0])
    mail.copy(email_id[0], 'Birthdays')


def delete_todays_email_from_oldfolder():
    print('DELETING:', email_id[0])
    mail.store(email_id[0], '+FLAGS', '(\Deleted)')
    mail.expunge()


def check_todays_email_was_moved():
    mail.select('Birthdays')
    response_ok, moved_email_id = mail.search(None, todays_email)
    print('MOVED:', moved_email_id)


def close_connection():
    mail.close()
    mail.logout()
    print('CONNECTION CLOSED')


copy_todays_email_to_newfolder()
delete_todays_email_from_oldfolder()
check_todays_email_was_moved()
close_connection()
