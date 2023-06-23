import smtplib
import os

email_tls = os.environ.get("MAIL_TLS")
email_ssl = os.environ.get("MAIL_SSL")
email_sender = os.environ.get("MAIL_SENDER")
email_password= os.environ.get("MAIL_PASSWORD")
email_receiver = os.environ.get("MAIL_RECEIVER")
email_smtp = os.environ.get("MAIL_SMTP")

def print_env():
    print(email_tls)
    print(email_ssl)
    print(email_sender)
    print(email_password)
    print(email_receiver)
    print(email_smtp)

print_env()

with smtplib.SMTP(host=email_smtp, port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_sender, email_password)

    subject = "Test email"
    body = "Hello World"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(email_sender, email_receiver, msg)

    print("Email sent successfully")
