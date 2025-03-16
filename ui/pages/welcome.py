# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class WelcomePage(Page):
    STR = 'welcome'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        page_title = ui.Text(
            self,
            (0, 50),
            'Welcome to Falcon Finance',
            ('Nunito', 70, True, False)
        )
        ui.center(page_title)

        image = ui.Image(
            self,
            (0, page_title.bottom + 50),
            'HRHS_logo.png',
            size=(300, 300)
        )
        ui.center(image)

        login = ui.TextButton(
            self,
            'Login To Account',
            ('Nunito', 25),
            (0, image.bottom + 75),
            lambda: manager.go_to('login'),
            padding=(40, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(login)

        create = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 25),
            (0, login.bottom + 40),
            lambda: manager.go_to('create_account'),
            padding=(40, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(create)

