import smtplib
from email.message import EmailMessage

# Argument Descriptions:
# host = email host like gmail.com, outlook.com, etc...
# sender_email = sender email address (must be a valid host email)
# sender_password = the sender's email password
# recipient_email = recipient email address
# subject = the email subject line
# content = the body of the email
def send_email(host:str,sender_email:str,sender_password:str,recipient_email:str,subject:str,content:str) -> bool:
    result = False
    try:
        # connet to email host, use tls, login to email
        mail=smtplib.SMTP(host=f'smtp.{host}', port=587)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_email,sender_password)

        # configure email message data
        em = EmailMessage()
        em.set_content(content)
        em["Subject"] = subject
        em["From"] = sender_email
        em["To"] = recipient_email
 
        # send mail and exit
        mail.send_message(msg=em)
        mail.close()
        result = True
    except Exception as e:
        result = False
        print(f"Error in send_email(): {str(e)}")

    return result