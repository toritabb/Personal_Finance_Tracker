# local
import ui
import os
import pickle
import file
from .page import Page, PageManagerBase
from constants import SCREEN_W, SCREEN_H
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type
from file import get_global_path

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
our_email = 'falconfinancehelp@gmail.com'
CLIENT_SECRET_FILE = get_global_path('credentials.json')

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
service = gmail_authenticate()

class ContactPage(Page):
    STR = 'contact'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        def add_attachment(message, filename):
            content_type, encoding = guess_mime_type(filename)
            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'
            main_type, sub_type = content_type.split('/', 1)
            if main_type == 'text':
                fp = open(filename, 'rb')
                msg = MIMEText(fp.read().decode(), _subtype=sub_type)
                fp.close()
            elif main_type == 'image':
                fp = open(filename, 'rb')
                msg = MIMEImage(fp.read(), _subtype=sub_type)
                fp.close()
            elif main_type == 'audio':
                fp = open(filename, 'rb')
                msg = MIMEAudio(fp.read(), _subtype=sub_type)
                fp.close()
            else:
                fp = open(filename, 'rb')
                msg = MIMEBase(main_type, sub_type)
                msg.set_payload(fp.read())
                fp.close()
            filename = os.path.basename(filename)
            msg.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(msg)
        def build_message(destination, obj, body, attachments=[]):
            if not attachments: # no attachments given
                message = MIMEText(str(body))
                message['to'] = destination
                message['from'] = our_email
                message['subject'] = obj
            else:
                message = MIMEMultipart()
                message['to'] = destination
                message['from'] = our_email
                message['subject'] = obj
                message.attach(MIMEText(str(body)))
                for filename in attachments:
                    add_attachment(message, filename)
            return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
        def send_message(service, destination, obj, body, attachments=[]):
            return service.users().messages().send(
            userId="me",
            body=build_message(destination, obj, body, attachments)
            ).execute()

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'Contact Page',
            ('Nunito', 40, True, False)
        )

        email = ui.Text(
            self,
            (300, 0),
            'falconfinancehelp@gmail.com',
            ('Nunito', 75)
        )
        ui.center(email, axis='x')
        ui.center(email, axis='y')
            

        contact = ui.Text(
            self,
            (0, email.top - 50),
            'Conatct us at',
            ('Nunito', 50)
        )

        ui.center(contact, axis='x') # center the text on the x

        # Add the question entry box and submit button
        email = ui.misc.Pointer('')
        ui.Textbox(
            self,
            email,
            ('Nunito', 20),
            (SCREEN_W // 2 - 150, 450),
            (300, 40),
            border_thickness=2,
            corner_radius=5
        )

        send = ui.TextButton(
            self,
            'Send',
            ('Nunito', 20),
            (0, 540),
            command=lambda :send_message(service, "falconfinancehelp@gmail.com", "Suppport Ticket", 
            email.get()),
            padding=(15, 7),
            border_thickness=4,
        )
        ui.center(send, axis="x")


        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=4
        )
            # you can remove these, they are just placeholders so you know what page it is and can return

