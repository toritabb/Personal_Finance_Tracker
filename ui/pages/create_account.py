# local
import ui
from .page import Page, PageManagerBase
from constants import SCREEN_W, SCREEN_H



class CreateAccountPage(Page):
    STR = 'create_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        # Title
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 100),
            'Create Account',
            ('Nunito', 48, True, False)
        )

        # Username field
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 200),
            'Username:',
            ('Nunito', 24)
        )
        
        username = ui.misc.Pointer('')
        ui.Textbox(
            self,
            username,
            ('Nunito', 20),
            (SCREEN_W // 2 - 150, 240),
            (300, 40),
            border_thickness=2,
            corner_radius=5
        )

        # Password field
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 300),
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
            (SCREEN_W // 2 - 150, 340),
            (300, 40),
            validation_function=password_validator,
            border_thickness=2,
            corner_radius=5
        )

        # Confirm Password field
        ui.Text(
            self,
            (SCREEN_W // 2 - 150, 400),
            'Confirm Password:',
            ('Nunito', 24)
        )
        
        confirm_password = ui.misc.Pointer('')
        confirm_display = ui.misc.Pointer('')
        
        def confirm_validator(text: str) -> bool:
            confirm_password.set(text)  # Store actual confirmation
            confirm_display.set('*' * len(text))  # Display asterisks
            return True

        ui.Textbox(
            self,
            confirm_display,
            ('Nunito', 20),
            (SCREEN_W // 2 - 150, 440),
            (300, 40),
            validation_function=confirm_validator,
            border_thickness=2,
            corner_radius=5
        )

        # Create Account button
        ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 24),
            (SCREEN_W // 2 - 100, 520),
            command=lambda: self._handle_create_account(
                username.get(),
                password.get(),
                confirm_password.get()
            ),
            padding=(30, 15),
            border_thickness=3,
            corner_radius=8
        )

        # Back to Login link
        ui.TextButton(
            self,
            'Back to Login',
            ('Nunito', 20),
            (SCREEN_W // 2 - 70, 600),
            command=lambda: manager.go_to('login'),
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

    def _handle_create_account(self, username: str, password: str, confirm_password: str) -> None:
        if not username or not password:
            print("Username and password are required")
            return
            
        if password != confirm_password:
            print("Passwords do not match")
            return

        # TODO: Implement actual account creation logic
        print(f"Creating account - Username: {username}")

