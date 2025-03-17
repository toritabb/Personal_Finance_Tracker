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
            (0, 65),
            'Create Account',
            ('Nunito', 65, True, False)
        )
        ui.center(title)

        # Name field
        name_label = ui.Text(
            self,
            (0, title.bottom + 60),
            'Name',
            ('Nunito', 25)
        )

        name_ptr = ui.misc.Pointer('')
        name_box = ui.Textbox(
            self,
            name_ptr,
            ('Nunito', 20),
            (0, name_label.bottom + 7),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(name_label, name_box)

        # Username field
        email_label = ui.Text(
            self,
            (0, name_box.bottom + 25),
            'Email',
            ('Nunito', 25)
        )

        email_ptr = ui.misc.Pointer('')
        email_box = ui.Textbox(
            self,
            email_ptr,
            ('Nunito', 20),
            (0, email_label.bottom + 7),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(email_label, email_box)

        # Password field
        password_label = ui.Text(
            self,
            (0, email_box.bottom + 25),
            'Password',
            ('Nunito', 25)
        )

        password_ptr = ui.misc.Pointer('')
        password_display_ptr = ui.misc.Pointer('')
        password_box = ui.Textbox(
            self,
            password_display_ptr,
            ('Nunito', 20),
            (0, password_label.bottom + 7),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(password_label, password_box)

        # link the password so it puts ***** instead of the actual password
        def password_hider(ptr: ui.misc.Pointer[str]) -> None:
            new = ptr.get()
            current = password_ptr.get()

            # if they deleted a character
            if len(new) < len(current):
                password_ptr.set_no_listen(current[:len(new)])

            # if they typed or pasted
            elif len(new) > len(current):
                password_ptr.set_no_listen(current + new[len(current):])

                password_display_ptr.set_no_listen('*' * len(new))

        password_display_ptr.listen(password_hider)

        # Confirm password field
        confirm_password_label = ui.Text(
            self,
            (0, password_box.bottom + 25),
            'Confirm Password',
            ('Nunito', 25)
        )

        confirm_password_ptr = ui.misc.Pointer('')
        confirm_password_display_ptr = ui.misc.Pointer('')
        confirm_password_box = ui.Textbox(
            self,
            confirm_password_display_ptr,
            ('Nunito', 20),
            (0, confirm_password_label.bottom + 7),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(confirm_password_label, confirm_password_box)

        # link the password so it puts ***** instead of the actual password
        def confirm_password_hider(ptr: ui.misc.Pointer[str]) -> None:
            new = ptr.get()
            current = confirm_password_ptr.get()

            # if they deleted a character
            if len(new) < len(current):
                confirm_password_ptr.set_no_listen(current[:len(new)])

            # if they typed or pasted
            elif len(new) > len(current):
                confirm_password_ptr.set_no_listen(current + new[len(current):])

                confirm_password_display_ptr.set_no_listen('*' * len(new))

        confirm_password_display_ptr.listen(confirm_password_hider)

        # Create Account button
        create_button = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 24),
            (0, confirm_password_box.bottom + 60),
            command=lambda: self._handle_create_account(
                name_ptr.get(),
                email_ptr.get(),
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

    def _handle_create_account(self, name: str, email: str, password: str, confirm_password: str) -> None:
        # needs name, email, password
        if not name or not email or not password:
            print('Name, email, and password are required!')

            return
        
        # passwords must match
        if password != confirm_password:
            print('Passwords do not match!')

            return

        # can't already be a user with that email
        if data_manager.user_exists(email):
            print('Account with that email already exists!')

            return

        # Create new user
        data_manager.create_user(name, email, password)

        print('Account created successfully!')

        # Return to login page after successful account creation
        self._manager.go_to('login')

