import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ravi070589@gmail.com"
    password = "avhwambbpkraxawx"
    #password = os.getenv("PASSWORD")
    """here above we are trying to save the password in plain text so we have created env variable in windows and saved
    the password as PASSWORD variable"""

    receiver = "ravi070589@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
