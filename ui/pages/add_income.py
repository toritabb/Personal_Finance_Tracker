# local
import ui
from .page import Page, PageManagerBase



class AddIncomePage(Page):
    STR = 'add_income'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        page_title = ui.Text(
            self,
            (0, 50),
            'Add Income Source',
            ('Nunito', 50, True, False)
        )
        ui.center(page_title, axis='x')

        # recurring toggle
        recurring = ui.Canvas(self, (0, 250, 300, 100))
        
        recurring_title = ui.Text(
            recurring,
            (10, 10),
            'Recurring',
            ('Nunito', 20)
        )
        ui.center(recurring_title, axis='x')
        
        recurring_toggle = ui.Text(
            recurring,
            (0, 50),
            'Add Income Source',
            ('Nunito', 50, True, False)
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

