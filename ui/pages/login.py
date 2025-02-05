# local
import ui
from constants import SCREEN_W, SCREEN_H
from data import data_manager
from .page import Page, PageManagerBase



class LoginPage(Page):
    STR = 'login'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)
        self._manager = manager  # Store the manager as instance variable

        # Title
        login_title = ui.Text(
            self,
            (0, 100),
            'Login',
            ('Nunito', 48, True, False)
        )

        ui.center(login_title)

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
        login_btn = ui.TextButton(
            self,
            'Login',
            ('Nunito', 24),
            (0, 480),  # Initial x position will be centered
            command=lambda: self._handle_login(username.get(), password.get()),
            padding=(30, 15),
            border_thickness=3,
            corner_radius=8
        )
        ui.center(login_btn, axis='x')  # Center horizontally

        # Create Account link
        create_account_btn = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 20),
            (0, 560),  # Initial x position will be centered
            command=lambda: self._manager.go_to('create_account'),
            padding=(15, 7),
            border_thickness=2,
            corner_radius=5
        )
        ui.center(create_account_btn, axis='x')  # Center horizontally

        # Back button
        ui.TextButton(
            self,
            'Back',
            ('Nunito', 20),
            (25, SCREEN_H - 60),
            command=lambda: self._manager.back(),
            padding=(15, 7),
            border_thickness=2,
            corner_radius=5
        )

    def _handle_login(self, username: str, password: str) -> None:
        if not username or not password:
            print("Username and password are required")
            return

        # Attempt to authenticate and get the user
        user = data_manager.authenticate_user(username, password)
        if user:
            # Store the current user
            data_manager.set_current_user(user)
            print("Login successful!")
            self._manager.go_to('accounts')  # Navigate to accounts page after successful login
        else:
            print("Invalid username or password")

