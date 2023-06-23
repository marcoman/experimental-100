'''
This example shows us how to connect to our SMTP server and send an email.  
I use environment variables to define the sender and recipient, as well as the credentials.
On the backend, I configured my environment so I don't have to check any files into github, which is presently a public repo.

'''
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


def send_email():
    '''
    This function sends an email using the SMTP server.
    '''
    with smtplib.SMTP(host=email_smtp, port=email_tls) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email_sender, email_password)

        subject = "Test email"
        body = "Hello World"

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(email_sender, email_receiver, msg)

        print("Email sent successfully")

print_env()

