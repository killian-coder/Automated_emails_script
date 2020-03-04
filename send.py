from utility import Utility

recipient = "email  where its going"
message = 'Hallo'
subject ='Testing one  two'
attachment =[r'''/Users/admin/Downloads/SmartRevision_Cred.xlsx''']
sender = ''
cc=None
host='www.gmail.com'

Utility.send_email(recipient,message,subject,attachment,sender,cc=cc)