# local
import ui
import file
from data import data_manager
from ui.theme import invert
from .page import Page, PageManagerBase



class SettingsPage(Page):
    STR = 'settings'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        title = ui.Text(
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

        # Notifications setting
        notif_text = ui.Text(
            self,
            (25, title.bottom + 50),
            'Notifications',
            ('Nunito', 20),
            align_x='left'
        )

        ui.Toggle(
            self,
            (notif_text.right + 15, notif_text.centery - 12),
            25,
            ui.Pointer(True),
            border_thickness=4,
            corner_radius=0
        )

        # Dark mode setting
        dark_mode_text = ui.Text(
            self,
            (25, notif_text.bottom + 30),
            'Dark Mode',
            ('Nunito', 20),
            align_x='left'
        )

        dark_mode_ptr = ui.Pointer(False)
        dark_mode_toggle = ui.Toggle(
            self,
            (dark_mode_text.right + 15, dark_mode_text.centery - 12),
            25,
            dark_mode_ptr,
            border_thickness=4,
            corner_radius=0
        )

        dark_mode_ptr.listen(lambda _: invert()) # TODO: FIX TS

        # Export data button
        def export_user_data() -> None:
            current_user = data_manager.user

            if not current_user:
                print('No user logged in')
                return
                
            export_path = f'C:/Users/talan/OneDrive/Desktop/{current_user.name}.json'

            if data_manager.export_current_user_data(export_path):
                print(f'Data exported successfully to {export_path}')

            else:
                print('Failed to export data')

        export_button = ui.TextButton(
            self,
            'Export Account Data',
            ('Nunito', 20),
            (25, dark_mode_text.bottom + 40),
            command=export_user_data,
            padding=(15, 7),
            border_thickness=3,
            corner_radius=8
        )

