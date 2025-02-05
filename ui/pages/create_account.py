# local
import ui
from constants import SCREEN_W, SCREEN_H
from data import data_manager
from .page import Page, PageManagerBase



class CreateAccountPage(Page):
    STR = 'create_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)
        self._manager = manager  # Store the manager as instance variable

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
        create_btn = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 24),
            (0, 520),  # Initial x position will be centered
            command=lambda: self._handle_create_account(
                username.get(),
                password.get(),
                confirm_password.get()
            ),
            padding=(20, 10),
            border_thickness=3,
            corner_radius=8
        )
        ui.center(create_btn, axis='x')  # Center horizontally

        # Back to Login link
        back_btn = ui.TextButton(
            self,
            'Back to Login',
            ('Nunito', 20),
            (0, SCREEN_H - 60),
            command=lambda: self._manager.go_to('login'),
            padding=(15, 7),
            border_thickness=2,
            corner_radius=5
        )
        ui.center(back_btn, axis='x')  # Center horizontally

    def _handle_create_account(self, username: str, password: str, confirm_password: str) -> None:
        if not username or not password:
            print("Username and password are required")
            return
            
        if password != confirm_password:
            print("Passwords do not match")
            return

        if data_manager.user_exists(username):
            print("Username already exists")
            return

        # Create new user
        user = data_manager.create_user(username, password)
        
        # Add a default checking account for the user
        user.add_account(
            name=f"Savings Account",
            type='savings',
            balance=0
        )
        
        # Save changes
        data_manager.save()
        
        print("Account created successfully!")
        self._manager.go_to('login')  # Return to login page after successful account creation

