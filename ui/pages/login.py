# local
import ui
from constants import SCREEN_W, SCREEN_H
from data import data_manager
from .page import Page, PageManagerBase



class LoginPage(Page):
    STR = 'login'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # Title
        ui.Text(
            self,
            (SCREEN_W // 2 - 100, 100),
            'Login',
            ('Nunito', 48, True, False)
        )

        # Username field
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 250),
            'Username:',
            ('Nunito', 24)
        )
        
        username = ui.misc.Pointer('')
        ui.Textbox(
            self,
            username,
            ('Nunito', 20),
            (SCREEN_W // 2 - 150, 290),
            (300, 40),
            border_thickness=2,
            corner_radius=5
        )

        # Password field
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 350),
            'Password:',
            ('Nunito', 24)
        )
        
        password = ui.misc.Pointer('')
        password_display = ui.misc.Pointer('')
        
        def password_validator(text: str) -> bool:
            password.set(text)  # Store actual password
            password_display.set('*' * len(text))  # Display asterisks
            return True

        ui.Textbox(
            self,
            password_display,
            ('Nunito', 20),
            (SCREEN_W // 2 - 150, 390),
            (300, 40),
            validation_function=password_validator,
            border_thickness=2,
            corner_radius=5
        )

        # Login button
        ui.TextButton(
            self,
            'Login',
            ('Nunito', 24),
            (SCREEN_W // 2 - 60, 480),
            command=lambda: self._handle_login(username.get(), password.get()),
            padding=(30, 15),
            border_thickness=3,
            corner_radius=8
        )

        # Create Account link
        ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 20),
            (SCREEN_W // 2 - 70, 560),
            command=lambda: manager.go_to('create_account'),
            padding=(15, 7),
            border_thickness=2,
            corner_radius=5
        )

        # Back button
        ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, SCREEN_H - 60),
            command=lambda: manager.back(),
            padding=(15, 7),
            border_thickness=2,
            corner_radius=5
        )

    def _handle_login(self, username: str, password: str) -> None:
        # TODO: Implement actual login logic
        print(f"Login attempt - Username: {username}")


