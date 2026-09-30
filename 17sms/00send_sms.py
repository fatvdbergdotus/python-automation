# Download the helper library from 
# and https://www.twilio.com/docs/twilio-cli/getting-started/install
# py -3.12 -m pip install twilio

import os
from twilio.rest import Client

def send_sms(to: str, from_: str, body: str ) -> str:
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = "ACb41e2bbd325dec52fc3a3865cca58d8e"
    auth_token = "992e09f72765e2e1d1021efbaf3f9364"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to,
        from_=from_,
        body=body,
    )

    return message.sid

if __name__ == "__main__":
    # send a single test SMS
    send_sms(
        to="+31613236363",
        from_="+4915888620339",
        body="sms_appointment_reminders",
    )   


    # send an sms every 10 minutes forever
    # uncomment the following lines to enable sending SMS every 10 minutes
    # import time

    # while True:
    #    send_sms(
    #        to="+31613236363",
    #        from_="+4915888620339",
    #        body="sms_appointment_reminders",
    #    )
    #    time.sleep(600)  # wait for 10 minutes


    # send an sms every day at 17:00
    # uncomment the following lines to enable sending SMS every day at 17:00
    # import schedule
    # import time

    # def job():
    #     send_sms(
    #         to="+31613236363",
    #         from_="+4915888620339",
    #         body="sms_appointment_reminders",
    #     )

    # schedule.every().day.at("17:00").do(job)

    # while True:
    #     schedule.run_pending()
    #     time.sleep(60)  # wait for 1 minute


    # schedule sms sending using python anywhere
    # create a new file on pythonanywhere with the following content:
    # from your_module import send_sms
    # send_sms(
    #     to="+31613236363",
    #     from_="+4915888620339",
    #     body="sms_appointment_reminders",
    # )
    # then schedule it using the pythonanywhere web interface
    # make sure to have a paid account on PythonAnywhere to enable scheduled tasks