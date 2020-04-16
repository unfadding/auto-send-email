*** Settings ***
Documentation          Check if the e-mail is arriving accordingly
Variables               get_email.py
Variables               email_parser.py

*** Keywords ***
You have a connected mailbox
    Should Be Equal        ${type_mail}                               OK

You get intended email
    Should Contain         Decode Bytes To String ${raw_email}        birthday-all

Mailbox has intended email 
    Should Contain         Decode Bytes To String ${decoded_email}    http://communications

You check email content
    Should Contain         Decode Bytes To String ${email_message}    fonts.googleapis.com/css?family=Roboto

It brings list of parsed emails
    Should Not Be Empty     ${email_list}