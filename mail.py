import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
import time
from akun import *
def proses():
    timestr = time.strftime("%Y%m%d-%H%M")
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Sistem Menemukan Indikasi Manusia'
    
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'Manusia.jpg'
    
    with open(attach_file_name, 'rb') as fp:
        img = MIMEImage(fp.read())
        message.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
        message.attach(img)
    
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() 
    session.login(sender_address, sender_pass) 
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
