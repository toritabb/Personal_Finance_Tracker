# local
import ui
from .page import Page, PageManagerBase



LEGAL = '''
1. Introduction
Welcome to Falcon Finance (the "Application").
By using this Application, you agree to be bound by these Terms of Service ("Terms").
If you do not agree to these Terms, do not use the Application.

2. Disclaimer
The Application is provided "as is" and "as available" without any warranties, express or implied.
We do not guarantee the accuracy, reliability, or availability of the Application.
Your use of the Application is at your own risk.
We are not responsible for any damages, losses, or issues resulting from your use of the Application.

3. User Responsibilities
You agree to use the Application lawfully and responsibly. You may not use the Application for
any illegal activities or in a manner that may cause harm to others.
We reserve the right to terminate access for any user who violates these Terms.

4. Limitation of Liability
To the fullest extent permitted by law, we are not liable for any direct, indirect, incidental,
or consequential damages arising from your use or inability to use the Application.

5. Intellectual Property
All content, features, and functionality of the Application are owned by us or our licensors and
are protected by copyright, trademark, and other intellectual property laws.
Unauthorized use of any materials is prohibited.

6. Changes to the Terms
We reserve the right to modify these Terms at any time. Continued use of the Application after changes
constitute acceptance of the new Terms.

7. Contact Information
For any questions or concerns regarding these Terms, contact us at falconfinancehelp@gmail.com.
'''

LEGAL_HEADERS = [
    '1. Introduction',
    '2. Disclaimer',
    '3. User Responsibilities',
    '4. Limitation of Liability',
    '5. Intellectual Property',
    '6. Changes to the Terms',
    '7. Contact Information'
]

LEGAL_TEXT = [
    'Welcome to Falcon Finance (the "Application"). \nBy using this Application, you agree to be bound by these Terms of Service ("Terms"). \nIf you do not agree to these Terms, do not use the Application.',
    'The Application is provided "as is" and "as available" without any warranties, express or implied. \nWe do not guarantee the accuracy, reliability, or availability of the Application. \nYour use of the Application is at your own risk. \nWe are not responsible for any damages, losses, or issues resulting from your use of the Application.',
    'You agree to use the Application lawfully and responsibly. You may not use the Application for \nany illegal activities or in a manner that may cause harm to others. \nWe reserve the right to terminate access for any user who violates these Terms.',
    'To the fullest extent permitted by law, we are not liable for any direct, indirect, incidental, \nor consequential damages arising from your use or inability to use the Application.',
    'All content, features, and functionality of the Application are owned by us or our licensors and \nare protected by copyright, trademark, and other intellectual property laws. \nUnauthorized use of any materials is prohibited.',
    'We reserve the right to modify these Terms at any time. Continued use of the Application after changes \nconstitute acceptance of the new Terms.',
    'For any questions or concerns regarding these Terms, contact us at falconfinancehelp@gmail.com.'
]



class LegalPage(Page):
    STR = 'legal'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        title = ui.Text(
            self,
            (0, 50),
            'Legal Page',
            ('Nunito', 50, True, False)
        )
        ui.center(title)

        y = title.bottom + 65

        for header, text in zip(LEGAL_HEADERS, LEGAL_TEXT):
            head = ui.Text(
                self,
                (350, y),
                header,
                ('Nunito', 17, True, False)
            )

            y = head.bottom + 5

            txt = ui.Text(
                self,
                (350, y),
                text,
                ('Nunito', 14)
            )

            y = txt.bottom + 15

        back_button = ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, 660),
            command=lambda: manager.back(),
            padding=(15, 7)
        )

