# local
import ui
from constants import SCREEN_W, SCREEN_H
from data import data_manager
from .page import Page, PageManagerBase



class LoginPage(Page):
    STR = 'login'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)
        self._manager = manager

        # Title
        login_title = ui.Text(
            self,
            (0, 100),
            'Login',
            ('Nunito', 65, True, False)
        )
        ui.center(login_title)

        # Username
        username_label = ui.Text(
            self,
            (0, login_title.bottom + 75),
            'Username:',
            ('Nunito', 25)
        )

        username_ptr = ui.misc.Pointer('')
        username_box = ui.Textbox(
            self,
            username_ptr,
            ('Nunito', 20),
            (0, username_label.bottom + 10),
            (300, -1),
            padding=7,
            corner_radius=5
        )
        ui.center(username_label, username_box)

        # Password
        password_label = ui.Text(
            self,
            (0, username_box.bottom + 30),
            'Password:',
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
            padding=7,
            corner_radius=5
        )
        ui.center(password_label, password_box)

        # link the password so it puts ***** instead of the actual password
        def password_hider(ptr: ui.misc.Pointer[str]) -> None:
            text = ptr.get()

            if text != ('*' * len(text)):
                password_ptr.set(text)

                password_display_ptr.set('*' * len(text))

        password_display_ptr.listen(password_hider)

        # Login button
        login_button = ui.TextButton(
            self,
            'Login',
            ('Nunito', 30),
            (0, password_box.bottom + 85),
            command=lambda: self._handle_login(username_ptr.get(), password_ptr.get()),
            padding=(40, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(login_button)

        # Create Account link
        create_account_button = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 20),
            (0, login_button.bottom + 50),
            command=lambda: self._manager.go_to('create_account'),
            padding=(25, 10),
            border_thickness=0,
            colors='button_accent'
        )
        ui.center(create_account_button)

    def _handle_login(self, username: str, password: str) -> None:
        if not username or not password:
            print('Username and password are required')

            return

        # Attempt to authenticate and get the user
        user = data_manager.authenticate_user(username, password)

        if user:
            # Store the current user
            data_manager.set_current_user(user)

            print('Login successful!')

            self._manager.go_to('accounts')  # Navigate to snapshot page after successful login

        else:
            print('Invalid username or password')

