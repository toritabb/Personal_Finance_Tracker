# local
import ui
from .page import Page, PageManagerBase



LEGAL_TEXT = '''1. Introduction
Welcome to Falcon Finance (the "Application"). By using this Application, you agree to be bound by these Terms of Service ("Terms"). 
If you do not agree to these Terms, do not use the Application.


2. Disclaimer
The Application is provided "as is" and "as available" without any warranties, express or implied. 
We do not guarantee the accuracy, reliability, or availability of the Application. Your use of the Application is at your own risk. 
We are not responsible for any damages, losses, or issues resulting from your use of the Application.

3. User Responsibilities
You agree to use the Application lawfully and responsibly. You may not use the Application for any illegal activities or in a manner that may cause harm to others. 
We reserve the right to terminate access for any user who violates these Terms.

4. Limitation of Liability
To the fullest extent permitted by law, we are not liable for any direct, indirect, incidental, or consequential damages arising from your use or inability to use the Application.

5. Intellectual Property
All content, features, and functionality of the Application are owned by us or our licensors and are protected by copyright, trademark, and other intellectual property laws. 
Unauthorized use of any materials is prohibited.

6. Changes to the Terms
We reserve the right to modify these Terms at any time. Continued use of the Application after changes constitute acceptance of the new Terms.

7. Contact Information
For any questions or concerns regarding these Terms, contact us at falconfinancehelp@gmail.com.
'''



class LegalPage(Page):
    STR = 'legal'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'Legal Page',
            ('Nunito', 40, True, False)
        )

        disclaimer = ui.Text(
            self,
            (300, 0),
            LEGAL_TEXT,
            ('Nunito', 15)
        )
        ui.center(disclaimer, axis='xy')

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

