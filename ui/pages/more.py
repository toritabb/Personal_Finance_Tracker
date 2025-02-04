# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class MorePage(Page):
    STR = 'more'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

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

