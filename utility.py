import os, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

class Utility():

    def __init__(self):
        pass

    @staticmethod
    def send_email(recipient,message,subject,attachment=None,sender=None,cc=None,host='webmail.zamtel.co.zm'):
        """Sends email
        
        Arguments:
            recipient {str} -- email of the recipient
            message {str} -- message to send
            subject {str} -- the subject of the email
        
        Keyword Arguments:
            attachment {list} -- A list of absolute paths to the attachements (default: {None})
            sender {str} -- email of the sender (default: {None})
            cc {str} -- a string of emails to put in copy separated by semicolons (default: {None})
            host {str} -- email provider domain (default: {'webmail.zamtel.co.zm'})
        """
        port = 465
        password='password'

        context = ssl.create_default_context()

        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        connection = smtplib.SMTP(host, port)
        connection.ehlo()
        connection.starttls(context=context)
        connection.ehlo()
        connection.login(sender, password)

        msg = MIMEMultipart() 
        
        # setup the parameters of the message
        msg['From']=sender
        msg['To']=recipient
        msg['Subject']=subject
        msg['Cc']= cc
            
        ## add in the message body
        msg.attach(MIMEText(message, 'html'))

        if attachment is not None:
            for f in attachment:
                filename = f.split(os.path.sep)[-1]
                actual_file = MIMEApplication(open(f, "rb").read(), _subtype="txt")
                actual_file.add_header('Content-Disposition', f'attachment; filename={filename}')
                msg.attach(actual_file)

        text = msg.as_string()
        connection.send_message(msg)
        connection.quit()

    @staticmethod
    def is_dir(dir):
        """check if path points to a folder
        
        Arguments:
            dir {str} -- path to folder
        
        Returns:
            bool -- True means folder and False means not folder
        """
        return os.path.exists(dir) and os.path.isdir(dir)

    @staticmethod
    def is_file(dir):
        """check if path points to file
        
        Arguments:
            dir {str} -- path to file
        
        Returns:
            bool -- True means files and False means not file
        """
        return os.path.exists(dir) and os.path.isfile(dir)

    @staticmethod
    def get_files(dir):
        """gets a list of files from a specified path
        
        Arguments:
            dir {str} --path to file/files
        
        Returns:
            list -- if not empty a 2D list is returned, with the inner list containing absolute paths to files i.e [[fileA, fileB]], else if the outer list is empty, [] is returned 
        """
        return [files for (root, dirs, files) in os.walk(dir) if files]

    @staticmethod
    def create_dir(dir):
        """Creates a folder
        
        Arguments:
            dir {str} -- path to folder
        
        Returns:
            Bool -- True if successfull else False
        """
        try:
            os.makedirs(dir)
            return True
        except FileExistsError:
            return False
