import argparse
import getpass
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):

    toaddr = "saket.jain@opstree.com"
    
    msg = MIMEMultipart()
    
    msg['From'] = "Vishant sharma"
    msg['To'] = toaddr
    msg['Subject'] = "!@#$^&*("
    
    body = "jds fsg k d hgf k agcfbs"
    
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "NAME OF THE FILE WITH ITS EXTENSION"
    attachment = open("/home/vishant/email/apnimail.py", "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)

    def msgSender(email, password):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, toaddr, text)
        server.quit()

    if __name__ == "__main__":

        parser = argparse.ArgumentParser()

        parser.add_argument("email", help="Email address")
        parser.add_argument("password", help="Password")
        args = parser.parse_args()


        msgSender(args.email, args.password)

    s.enter(2, 1, do_something, (sc,))

s.enter(2, 1, do_something, (s,))
s.run()
