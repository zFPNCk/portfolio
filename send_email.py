import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ng4324757@gmail.com"
passwords = "kmht bwuc lzak nxqn"

receiver = "ng4324757@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, passwords)
    server.sendmail(username, receiver, message)