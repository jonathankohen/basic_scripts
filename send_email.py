# In [1]: import getpass
# In [2]: import smtplib
# In [3]: HOST = “smtp.gmail.com”
# In [4]: PORT = 465
# In [5]: username = “username@gmail.com”
# In [6]: password = getpass.getpass(“Provide Gmail password: “)
# Provide Gmail password:
# In [7]: server = smtplib.SMTP_SSL(HOST, PORT)
# In [8]: server.login(username, password)
# Out[8]: (235, b’2.7.0 Accepted’)
# In [9]: server.sendmail(
#   ...:     “from@domain.com”,
#   ...:      “to@domain.com”,
#   ...:     “An email from Python!”,
#   ...:     )
# Out[9]: {}
# In [8]: server.quit()
# Out[8]: (221, b’2.0.0 closing connection s1sm24313728ljc.3 - gsmtp’)