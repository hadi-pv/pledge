import smtplib

from email.message import EmailMessage

MY_EMAIL="shecan.pledge@gmail.com"
MY_PASS="pledgeshecan"



def send_email(to):
    message=EmailMessage()
    message['subject']="Pledge for She Can Campaign"
    message['from']=MY_EMAIL
    message['to']=to
    message.set_content("Pledge for She Can Campaign")
    html_message=open('ncore.html').read()
    message.add_alternative(html_message,subtype="html")

    with open("Pledge_SheCan.pdf","rb") as attach_file:
        pdf_name=attach_file.name
        pdf_data=attach_file.read()

    message.add_attachment(pdf_data, maintype='application', subtype='octet-stream', filename=pdf_name)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
        smtp.login(MY_EMAIL,MY_PASS)
        smtp.send_message(message)
