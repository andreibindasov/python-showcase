import smtplib
import ssl
import os


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("PYTHON_USER_EMAIL")
    phrase = os.getenv("PASSPHRASE")

    receiver = ["email1@email.com", "email2@email.com"]

    context = ssl.create_default_context()
    # subject = user_email
    message = user_message
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, phrase)
        server.sendmail(username, receiver, message)
