import smtplib
import config

def send_email(email,sub,body):
    message = 'subject : {}\n\n{}'.format(sub,body)
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(config.my_email,config.my_password)
    server.sendmail(config.my_email,email,message)
    server.quit()

send_email("nfraz007@gmail.com","checking smtp server","I have created a function which will take three parameter receiver's email,subject, and body")