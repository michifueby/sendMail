#!/bin/python *
# -*- coding: UTF-8 -*-
# autor:   Michael Füby 
# version: 1.0.2
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# Defined the log function
def log(log_path):
    try:
        global logger
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename=log_path,
                            level=logging.DEBUG,
                            format=LOG_FORMAT)
        logger = logging.getLogger()
        return True
    except:
        print "ATTENTION!\nThe logger is not active, all changes are not logged!"
        return False

# Defined the sendmail function
def sendMail(user, receiver, subject, body, password, server, port):
    try:
        msg = MIMEMultipart()
        msg['From'] = user
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        # Server outlet name and port are defined
        text = msg.as_string()
    except:
        print "An error with the 'MIME-Type' declaration has occurred!"
        if (logs == 1):
            logger.error("An error with the 'MIME-Type' declaration has occurred, required 'libraries are probably missing'!")
        return False

    try:
        server = smtplib.SMTP(server, port)
        # TLS connection is started
        server.starttls()
        # Server login with the data
    except:
        print "It couldn't connect to the server '" + server + ":" + port + "'!"
        if (logs == 1):
            logger.error("A connection to the server could not be established! Please check the address and port!")
            logger.info("Server: " +server+ ":" +port)
        return False

    try:
        # Mail user login
        server.login(user, password)
    except:
        print "User could not be logged in!\nPlease check your data!"
        if (logs == 1):
            logger.error("User could not be logged in! Check the information provided and then try again.")
        return False

    try:
        server.sendmail(user, receiver, text)
        server.quit()
        logger.info("Email was successfully sent!")
        logger.info("From: " +user+ "\nTo: " +receiver+ "\nTitle: " +subject+ "\nContent: " +body)
    except:
        return False
    return True


def main():
    # All settings are made here and all required data is specified
    # Start the logger
    if (log('sendmail_script.log') == False):
        print "Logger could not be created!"
        logs = 0
    else:
        logs = 1

    # Sender, password and recipient are defined
    user = 'test@test.com'
    password = 'test'
    receiver = 'test1@test.com'
    # The subject and the message are defined
    subject = 'Subject'
    body = 'The test was successful!'
    # Server and Port
    smtp_server = 'smtp.test.com'
    smtp_port = '25'

    if (sendMail(user, receiver, subject, body, password, smtp_server, smtp_port) == False):
        print "Mail was not sent!"
        logger.critical("Mail could not be sent!")
        logger.info("From: " +user+ "\nTo: " +receiver+ "\nTitle: " +subject+ "\nContent: " +body)
    exit()
main()
exit()
    
