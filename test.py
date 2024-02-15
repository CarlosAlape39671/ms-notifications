from azure.communication.email import EmailClient
from dotenv import load_dotenv
import os

class Test:

    def __init__(self, message, recipient, subject_line):
        self.message = message
        self.recipient = recipient
        self.subject_line = subject_line

    def send_the_email(self):
        response = False
        load_dotenv()
        try:
            connection_string = os.getenv("CONNECTION_STRING")
            client = EmailClient.from_connection_string(connection_string)

            message = {
                "senderAddress": os.getenv("SENDER_ADDRESS"),
                "recipients":  {
                    "to": [{"address": self.recipient }],
                },
                "content": {
                    "subject": self.subject_line,
                    "plainText": self.message,
                }
            }

            poller = client.begin_send(message)
            result = poller.result()
            response = True

        except Exception as ex:
            print(ex)

        return response