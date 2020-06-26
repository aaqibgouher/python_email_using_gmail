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

# This is my first project. In this project , what i have did is i have sended email using python. so here , i have written a function which will take three parameter namely receiver's email,subject and body.
# simply we have to pass all these parameters in the send_email() function . and then we have imported two things : first is out smtplib which is simplr mail transfer protocol, and secondly i have imported 
# config file. In  config, sender's email and pass will be there.and then simply we have to use some of the inbuilt function of smtp. then we can do it easily.