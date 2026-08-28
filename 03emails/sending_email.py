import yagmail
import time

sender = 'freek23@gmail.com'
receiver = 'f@vdberg.us'
password = 'rkhy nqbj seom uune'
subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

# sends a single email
yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")

# sends the same email 5 times including a counter every 20 seconds
number = 1
while number<=5:
    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=receiver, subject=subject+" "+str(number), contents=contents)
    print("Email Sent!"+" "+str(number))
    time.sleep(20)
    number += 1

# sends an email at a certain time every day
while True:
    if time.strftime("%H:%M") == "16:30":
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email Sent at 16:30!")
        time.sleep(60)