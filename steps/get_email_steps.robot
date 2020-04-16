*** Settings ***
Resource          ../tests/get_email_tests.robot

*** Test Cases ***
Test intended e-mail presence at mailbox
  Given You have a connected mailbox
  When You get intended email
  Then Mailbox has intended email

Test E-mail Content
  Given You get intended email
  When You check email content
  Then It brings list of parsed emails