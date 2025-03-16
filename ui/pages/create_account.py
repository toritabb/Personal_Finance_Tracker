# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class CreateAccountPage(Page):
    STR = 'create_account'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)
        self._manager = manager  # Store the manager as instance variable

        # Title
        title = ui.Text(
            self,
            (0, 75),
            'Create Account',
            ('Nunito', 65, True, False)
        )
        ui.center(title)

        # Username field
        username_label = ui.Text(
            self,
            (0, title.bottom + 60),
            'Username',
            ('Nunito', 25)
        )

        username_ptr = ui.misc.Pointer('')
        username_box = ui.Textbox(
            self,
            username_ptr,
            ('Nunito', 20),
            (0, username_label.bottom + 10),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(username_label, username_box)

        # Password field
        password_label = ui.Text(
            self,
            (0, username_box.bottom + 30),
            'Password',
            ('Nunito', 25)
        )

        password_ptr = ui.misc.Pointer('')
        password_display_ptr = ui.misc.Pointer('')
        password_box = ui.Textbox(
            self,
            password_display_ptr,
            ('Nunito', 20),
            (0, password_label.bottom + 10),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(password_label, password_box)

        # link the password so it puts ***** instead of the actual password
        def password_hider(ptr: ui.misc.Pointer[str]) -> None:
            text = ptr.get()
            current = password_ptr.get()

            if len(text) < len(current):
                current = current[:len(text)]

            elif len(text) > len(current):
                password_ptr.set(current + text[len(current):])

                password_display_ptr.set('*' * len(text))

        password_display_ptr.listen(password_hider)

        # Confirm password field
        confirm_password_label = ui.Text(
            self,
            (0, password_box.bottom + 30),
            'Confirm Password',
            ('Nunito', 25)
        )

        confirm_password_ptr = ui.misc.Pointer('')
        confirm_password_display_ptr = ui.misc.Pointer('')
        confirm_password_box = ui.Textbox(
            self,
            confirm_password_display_ptr,
            ('Nunito', 20),
            (0, confirm_password_label.bottom + 10),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(confirm_password_label, confirm_password_box)

        # link the password so it puts ***** instead of the actual password
        def confirm_password_hider(ptr: ui.misc.Pointer[str]) -> None:
            text = ptr.get()
            current = confirm_password_ptr.get()

            if len(text) < len(current):
                current = current[:len(text)]

            elif len(text) > len(current):
                confirm_password_ptr.set(current + text[len(current):])

                confirm_password_display_ptr.set('*' * len(text))

        confirm_password_display_ptr.listen(confirm_password_hider)

        # Create Account button
        create_button = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 24),
            (0, confirm_password_box.bottom + 60),
            command=lambda: self._handle_create_account(
                username_ptr.get(),
                password_ptr.get(),
                confirm_password_ptr.get()
            ),
            padding=(40, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(create_button)

        # Back to Login link
        back_button = ui.TextButton(
            self,
            'Back to Login',
            ('Nunito', 20),
            (0, create_button.bottom + 40),
            command=lambda: self._manager.go_to('login'),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(back_button)

    def _handle_create_account(self, username: str, password: str, confirm_password: str) -> None:
        if not username or not password:
            print('Username and password are required')
            return
            
        if password != confirm_password:
            print('Passwords do not match')
            return

        if data_manager.user_exists(username):
            print('Username already exists')
            return

        # Create new user
        user = data_manager.create_user(username, password)
        
        # Add a default checking account for the user
        user.add_account(
            name=f'Savings Account',
            type='savings',
            balance=0
        )
        
        # Save changes
        data_manager.save()
        
        print('Account created successfully!')
        self._manager.go_to('login')  # Return to login page after successful account creation

