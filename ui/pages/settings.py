# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class SettingsPage(Page):
    STR = 'settings'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # you can remove these, they are just placeholders so you know what page it is and can return
        page_title = ui.Text(
            self,
            (25, 25),
            'Settings Page',
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

        text1 = ui.Text(
            self,
            (25, page_title.bottom + 50),
            'Notifications',
            ('Nunito', 20),
            align = 'left'
        )

        # notifications on or off
        notifToggle = ui.Toggle(
            self,
            (text1.right + 15, page_title.bottom + 47),
            25,
            ui.Pointer(True),
            border_thickness=4,
            corner_radius=0
        )
        # you can remove these, they are just placeholders so you know what page it is and can return

