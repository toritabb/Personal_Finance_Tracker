# local
import ui
import os
import pickle
import file
from .page import Page, PageManagerBase
from datetime import datetime
from googleapiclient.discovery import build, Resource
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



SCOPES = ['https://mail.google.com/']
CLIENT_SECRET_FILE = get_global_path('credentials.json')
EMIAL = 'falconfinancehelp@gmail.com'



def get_service() -> Resource:
    '''Request all access (permission to read/send/receive emails, manage the inbox, and more)'''

    creds = None

    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            print('loaded creds')

    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        print('creds need refresh')
        if creds and creds.expired and creds.refresh_token:
            print('refreshing creds')
            creds.refresh(Request())

        else:
            print('creds good')
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        # save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            print('creds saved')

    print('sending resource')
    return build('gmail', 'v1', credentials=creds)


def build_message(destination: str, subject, body):
    message = MIMEText(str(body))
    message['to'] = destination
    message['from'] = EMIAL
    message['subject'] = subject

    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service: Resource, destination: str, subject: str, body: str):
    return service.users().messages().send(     # type: ignore
        userId="me",
        body=build_message(destination, subject, body)
    ).execute()



class ContactPage(Page):
    STR = 'contact'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        try:
            service = get_service()

            self.init_online(service)

        except Exception as e:
            print(f'Failed to connect to the internet: {e}')

            self.init_offline()

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
        )

    def init_online(self, service: Resource) -> None:
        contact = ui.Text(
            self,
            (0, 40),
            'Contact Us',
            ('Nunito', 50, True, False),
        )

        our_email = ui.Text(
            self,
            (0, contact.bottom + 8),
            'at falconfinancehelp@gmail.com',
            ('Nunito', 25),
        )

        # User email
        email_label = ui.Text(
            self,
            (0, our_email.bottom + 60),
            'Email',
            ('Nunito', 20, True, False),
        )

        email_ptr = ui.misc.Pointer('')
        email_box = ui.Textbox(
            self,
            email_ptr,
            ('Nunito', 22),
            (0, email_label.bottom + 10),
            (500, -1),
            padding=7,
            corner_radius=5,
        )

        # User problem/message
        email_content_label = ui.Text(
            self,
            (0, email_box.bottom + 25),
            'How can we help?',
            ('Nunito', 20, True, False),
        )

        email_content_ptr = ui.misc.Pointer('')
        email_content_box = ui.Textbox(
            self,
            email_content_ptr,
            ('Nunito', 22),
            (0, email_content_label.bottom + 10),
            (750, 250),
            padding=7,
            corner_radius=5,
            align_y='top',
            multiline=True
        )
        ui.center(contact, our_email, email_label, email_box, email_content_label, email_content_box)

        # Send ts email
        send_button = ui.TextButton(
            self,
            'Send',
            ('Nunito', 20),
            (0, email_content_box.bottom + 50),
            ########## SENDS THE EMAIL HERE ############
            command=lambda: send_message(service, 'falconfinancehelp@gmail.com', 'Suppport Ticket', f'From: {email_ptr.get()}\n\n{email_content_ptr.get()}'),
            padding=(15, 7),
        )
        ui.center(send_button)

    def init_offline(self) -> None:
        wifi_symbol = ui.Image(
            self,
            (0, 120),
            'wifi_symbol.png'
        )
        ui.center(wifi_symbol)

        no_connection = ui.Text(
            self,
            (0, wifi_symbol.bottom + 120),
            'We\'re having trouble connecting to the internet!',
            ('Nunito', 50)
        )
        ui.center(no_connection)

        contact = ui.Text(
            self,
            (0, no_connection.bottom + 80),
            'You can contact us by email any time at:\nfalconfinancehelp@gmail.com',
            ('Nunito', 35),
            align_x='center',
            line_spacing=5
        )
        ui.center(contact)

