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

        padding_pages = (30, 7)

        title = ui.Text(
            self,
            (0, header.bottom + 20),
            'More Options',
            ('Nunito', 50, True, False)
        )
        ui.center(title, axis='x')

        faq_button = ui.TextButton(
            self,
            'FAQ',
            ('Nunito', 40),
            (title.left - 140, header.bottom + 150),
            lambda: manager.go_to('faq'),
            padding=padding_pages,
        )

        settings = ui.TextButton(
            self,
            'Settings',
            ('Nunito', 40),
            (title.right + 50, header.bottom + 150),
            lambda: manager.go_to('settings'),
            padding=padding_pages,
        )

        contact = ui.TextButton(
            self,
            'Contact',
            ('Nunito', 40),
            (title.right + 50, header.bottom + 350),
            lambda: manager.go_to('contact'),
            padding=padding_pages,
        )

        # log out button
        def _logout():
            data_manager.logout_user()

            manager.go_to('login')

            print('Successfully logged out')

        logout = ui.TextButton(
            self,
            'Log Out',
            ('Nunito', 40),
            (title.left - 150, header.bottom + 350),
            _logout,
            padding=padding_pages,
        )

        legal_button = ui.TextButton(
            self,
            'Legal',
            ('Nunito', 20),
            (1165, 660),
            lambda: manager.go_to('legal'),
            padding=(15, 7),
        )

