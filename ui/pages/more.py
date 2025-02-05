# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class MorePage(Page):
    STR = 'more'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        spacing_pages = 10
        padding_pages = (10, 5)
        border_thickness_pages = 3
        corner_radius_pages = -1

        faq_button = ui.TextButton(
            self,
            'FAQ',
            ('Nunito', 25),
            (500, 600),
            lambda: manager.go_to('faq'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        legal_button = ui.TextButton(
            self,
            'Legal',
            ('Nunito', 25),
            (500, 500),
            lambda: manager.go_to('legal'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        settings = ui.TextButton(
            self,
            'settings',
            ('Nunito', 25),
            (500, 400),
            lambda: manager.go_to('settings'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        contact = ui.TextButton(
            self,
            'contact',
            ('Nunito', 25),
            (500, 300),
            lambda: manager.go_to('contact'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        # log out button
        logOut = ui.TextButton(
            self,
            'Log Out',
            ('Nunito', 20),
            (25, 300),
            # needs account handling logic
            lambda: manager.go_to('create_account'),
            padding=(35, 7),
            border_thickness=3,
            corner_radius=-1
        )

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'More Page',
            ('Nunito', 40, True, False)
        )

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

