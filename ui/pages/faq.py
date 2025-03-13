# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



FAQ_TEXT = '''Q1: What is Falcon Finance?
A: Falcon Finance is a financial application designed to help users manage their finances efficiently and securely.

Q2: Is Falcon Finance free to use?
A: We believe in the necessity of open source software so Falcon Finance will always remain free .

Q3: How secure is my financial data?
A: We prioritize security and use encryption and other protective measures to safeguard your data. 
However, users should follow best security practices when using the Application.

Q4: How do I contact support?
A: You can reach our support team at falconfinancehelp@gmail.com or go to more then contact for any assistance
'''



class FAQPage(Page):
    STR = 'faq'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        page_title = ui.Text(
            self,
            (25, 25),
            'FAQ Page',
            ('Nunito', 40, True, False)
        )

        faq = ui.Text(
            self,
            (0, 150),
            FAQ_TEXT,
            ('Nunito', 23, True, False),
            align_x= 'center'
        )
        ui.center(faq, axis='x')

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=4
        )

