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
            (0, 25),
            'Welcome to Falcon Finance',
            ('Nunito', 75, True, False)
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
            'Log Into Existing Account',
            ('Nunito', 35),
            (0, image.bottom + 80),
            lambda: manager.go_to('login'),
            padding=(15, 7),
            border_thickness=4,
        )
        ui.center(login)

        create = ui.TextButton(
            self,
            'Create New Account',
            ('Nunito', 35),
            (0, login.bottom + 35),
            lambda: manager.go_to('create_account'),
            padding=(15, 7),
            border_thickness=4,
        )
        ui.center(create)

