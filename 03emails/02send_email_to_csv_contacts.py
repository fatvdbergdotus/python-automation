import yagmail
import pandas as pd

address_book = pd.read_csv('contacts.csv')

for name,receiver in address_book[['name', 'email']].values:
    sender = 'freek23@gmail.com'
    password = 'rkhy nqbj seom uune' # make a password at https://myaccount.google.com/apppasswords
    subject = "Hello " + name + "!"


    contents = """
    Here is the content of the email! 
    Hi!
    """

    # sends a single email
    yag = yagmail.SMTP(user=sender, password=password)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent to " + name + " at " + receiver)