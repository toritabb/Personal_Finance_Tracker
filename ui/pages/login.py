# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class LoginPage(Page):
    STR = 'login'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)
        self._manager = manager

        # Title
        title = ui.Text(
            self,
            (0, 100),
            'Login',
            ('Nunito', 65, True, False)
        )
        ui.center(title)

        # Username
        email_label = ui.Text(
            self,
            (0, title.bottom + 75),
            'Email',
            ('Nunito', 25)
        )

        email_ptr = ui.misc.Pointer('')
        email_box = ui.Textbox(
            self,
            email_ptr,
            ('Nunito', 20),
            (0, email_label.bottom + 10),
            (300, -1),
            padding=5,
            corner_radius=5
        )
        ui.center(email_label, email_box)

        # Password
        password_label = ui.Text(
            self,
            (0, email_box.bottom + 30),
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
            new = ptr.get()
            current = password_ptr.get()

            # if they deleted a character
            if len(new) < len(current):
                password_ptr.set_no_listen(current[:len(new)])

            # if they typed or pasted
            elif len(new) > len(current):
                password_ptr.set_no_listen(current + new[len(current):])

                password_display_ptr.set_no_listen('•' * len(new))

        password_display_ptr.listen(password_hider)

        # Login button
        login_button = ui.TextButton(
            self,
            'Login',
            ('Nunito', 30),
            (0, password_box.bottom + 85),
            command=lambda: self._handle_login(email_ptr.get(), password_ptr.get()),
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

    def _handle_login(self, email: str, password: str) -> None:
        if (not email) or (not password):
            print('Username and password are required!')

            return

        # Attempt to authenticate and get the user
        login_successful = data_manager.login_user(email, password)

        if login_successful:
            print('Login successful!')

            self._manager.go_to('accounts')

