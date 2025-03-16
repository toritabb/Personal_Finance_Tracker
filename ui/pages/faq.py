# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



FAQ_QUESTIONS = [
    'What is Falcon Finance?',
    'Is Falcon Finance free to use?',
    'How secure is my financial data?',
    'How do I contact support?'
]

FAQ_ANSWERS = [
    'Falcon Finance is a financial application designed to help users manage their finances efficiently and securely.',
    'We believe in the necessity of open source software so Falcon Finance will always remain free.',
    'We prioritize security and use encryption and other protective measures to safeguard your data.\nHowever, users should follow best security practices when using the Application.',
    'You can reach our support team by email at falconfinancehelp@gmail.com.\nAlternatively, go to the More and then Contact page for any assistance.'
]



class FAQPage(Page):
    STR = 'faq'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        page_title = ui.Text(
            self,
            (0, 50),
            'Frequently Asked Questions',
            ('Nunito', 50, True, False)
        )
        ui.center(page_title)

        y = page_title.bottom + 100

        for question, answer in zip(FAQ_QUESTIONS, FAQ_ANSWERS):
            q = ui.Text(
                self,
                (0, y),
                question,
                ('Nunito', 27, True, False)
            )
            ui.center(q)

            y = q.bottom + 7

            a = ui.Text(
                self,
                (0, y),
                answer,
                ('Nunito', 22)
            )
            ui.center(a)

            y = a.bottom + 30

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=4
        )

