# local
import ui
from data import data_manager
from .page import Page, PageManagerBase
from .header import HeaderPage



class MorePage(Page):
    STR = 'more'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        header = HeaderPage(self, manager)

        spacing_pages = 10
        padding_pages = (10, 5)
        border_thickness_pages = 3
        corner_radius_pages = -1

        title = ui.Text(
            self,
            (0, header.bottom + 20),
            'More Options',
            ('Nunito', 75)
        )
        ui.center(title, axis='x')

        faq_button = ui.TextButton(
            self,
            'FAQ',
            ('Nunito', 50),
            (title.left - 140, header.bottom + 150),
            lambda: manager.go_to('faq'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        settings = ui.TextButton(
            self,
            'Settings',
            ('Nunito', 50),
            (title.right + 50, header.bottom + 150),
            lambda: manager.go_to('settings'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        contact = ui.TextButton(
            self,
            'Contact',
            ('Nunito', 50),
            (title.right + 50, header.bottom + 350),
            lambda: manager.go_to('contact'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        # log out button
        logOut = ui.TextButton(
            self,
            'Log Out',
            ('Nunito', 50),
            (title.left - 150, header.bottom + 350),
            # needs account handling logic
            lambda: manager.go_to('create_account'),
            padding=(35, 7),
            border_thickness=3,
            corner_radius=-1
        )

        legal_button = ui.TextButton(
            self,
            'Legal',
            ('Nunito', 20),
            (1165, 660),
            lambda: manager.go_to('legal'),
            padding=(15, 7),
            border_thickness=4,
            corner_radius=corner_radius_pages
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

