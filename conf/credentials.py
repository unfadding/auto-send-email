import keyring

password = keyring.get_password("system", "password")
email = keyring.get_password("system", "email")
server = keyring.get_password("system", "server")