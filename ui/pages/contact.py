# local
import ui
from .page import Page, PageManagerBase



class ContactPage(Page):
    STR = 'contact'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

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

