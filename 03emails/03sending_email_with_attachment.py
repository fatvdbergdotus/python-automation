import yagmail
import time

sender = 'freek23@gmail.com'
receiver = 'f@vdberg.us'
password = 'rkhy nqbj seom uune' # make a password at https://myaccount.google.com/apppasswords
subject = "This is the subject!"
attachments = ["tiger.jpeg"]


contents1 = """
Here is the content of the email! 
Hi!
"""

# sends a single email with simple text content and an attachment
yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents1, attachments=attachments)
print("Email Sent!")

contents2 = [
    "<b>Hello!</b> This email uses <i>rich text</i> formatting.",
    "<ul><li>Item one</li><li>Item two</li></ul>",
    '<a href="https://python.org">Visit Python</a>',
]

# sends a single email with rich text formatting and an attachment
yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents2, attachments=attachments)
print("Email Sent!")
