import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ng4324757@gmail.com"
    passwords = "osfq jdej fbkc ebez"

    receiver = "ng4324757@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, passwords)
        server.sendmail(username, receiver, message)
    print('E-mail send successfully')