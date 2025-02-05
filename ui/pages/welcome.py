# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class WelcomePage(Page):
    STR = 'welcome'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'Welcome to Falcon Finance',
            ('Nunito', 40, True, False)
        )
        ui.center(page_title, axis= 'x')

        image = ui.Image(
            self,
            (25, page_title.bottom + 20),
            'HRHS_logo.png',
            size=(350, 350)
        )
        ui.center(image, axis= 'x')

        create = ui.TextButton(
            self,
            'Create New Account',
            ('Nunito', 50),
            (1165, image.bottom + 50),
            lambda: manager.go_to('create_account'),
            padding=(15, 7),
            border_thickness=4,
        )
        ui.center(create, axis= 'x')

        login = ui.TextButton(
            self,
            'Log Into Existing Account',
            ('Nunito', 50),
            (1165, create.bottom + 50),
            lambda: manager.go_to('login'),
            padding=(15, 7),
            border_thickness=4,
        )
        ui.center(login, axis= 'x')