import yagmail
import time

sender = 'freek23@gmail.com'
receiver = 'f@vdberg.us'
password = 'rkhy nqbj seom uune' # make a password at https://myaccount.google.com/apppasswords
subject = "This is the subject!"
attachments = ["tiger.jpeg"]


contents = """
Here is the content of the email! 
Hi!
"""

# sends a single email
yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents, attachments=attachments)
print("Email Sent!")