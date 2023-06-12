import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "andrei.bindasov73@gmail.com"
phrase = "nfwwqyfewygkgzzb"

receiver = ["abraxas777ainsoph@protonmail.com", "bindasov.andrei@gmail.com"]
# receiver = "bindasov.andrei@gmail.com"

context = ssl.create_default_context()

subject = "URGENT!!! HELP!!!"
message = """
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, phrase)
    server.sendmail(username, receiver, f"Subject:{subject}\n{message}")

