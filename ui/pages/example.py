# local
import ui
from data import data_manager
from .page import Page, PageManagerBase



class ExamplePage(Page):
    STR = 'example'

    def __init__(self, parent: ui.Canvas, manager: PageManagerBase) -> None:
        super().__init__(parent, manager)

        ########
        # TEXT #
        ########

        # normal, left align
        text1 = ui.Text(
            self,
            (25, 25),
            'The quick brown fox\njumps over the lazy dog.',
            ('Nunito', 20)
        )

        # bold
        text2 = ui.Text(
            self,
            (text1.right + 15, text1.top),
            'The five boxing\nwizards jump quickly.',
            ('Nunito', 20, True, False),
            align_x='center'
        )

        # italic
        text3 = ui.Text(
            self,
            (text1.left, text1.bottom + 15),
            'Jaded zombies acted\nquaintly but kept driving\ntheir oxen forward.',
            ('Nunito', 20, False, True),
            align_x='right',
            line_spacing=10
        )

        # bold and italic
        text4 = ui.Text(
            self,
            (text3.right + 10, text2.bottom + 15),
            'Pack my box with five dozen liquor jugs.',
            ('Nunito', 20, True, True),
        )

        ###################
        # CENTER ELEMENTS #
        ###################

        text_center = ui.Text(
            self,
            (0, 0),
            'Elements can be centered\nusing ui.center(element, axis=\'axis\')',
            ('Nunito', 20),
            align_x='center'
        )
        ui.center(text_center) # center the explanation on the x

        text_toggle_center = ui.Text(
            self,
            (0, text_center.bottom + 20),
            'Centered toggle:',
            ('Nunito', 20),
        )

        toggle_center = ui.Toggle(
            self,
            (text_toggle_center.right + 8, text_toggle_center.centery - 12),
            25,
            ui.Pointer(True),
            border_thickness=4,
            corner_radius=-1
        )
        ui.center(text_toggle_center, toggle_center, axis='x') # center the toggle and text on the x
        ui.center(text_center, text_toggle_center, toggle_center, axis='y') # center all on the y

        ###########
        # BUTTONS #
        ###########

        # plain button
        button1 = ui.Button(
            self,
            (25, text3.bottom + 25),
            (150, 40),
            lambda: print('empty button'),
            border_thickness=3,
            corner_radius=10
        )

        # button with text and a fixed width but not height
        button2 = ui.TextButton(
            self,
            'Accent',
            ('Nunito', 20),
            (button1.right + 10, button1.top),
            lambda: print('accent color button'),
            size=(200, -1), # fixed width of 200, and height that adjusts to text size
            padding=10,
            border_thickness=0,
            corner_radius=-1, # corners automatically fully rounded
            align_x='right',
            colors='button_accent' # uses the green colors to stand out more
        )

        # button with text and padding (the text IS centered)
        button3 = ui.TextButton(
            self,
            'Press Me!',
            ('Nunito', 20),
            (25, button1.bottom + 10),
            lambda: print('text button with no border'),
            padding=(35, 7),
            border_thickness=0,
            corner_radius=-1
        )

        # button that deletes itself
        button4 = ui.TextButton(
            self,
            'Delete',
            ('Nunito', 25),
            (button3.right + 10, button3.top),
            padding=7,
            border_thickness=3,
            corner_radius=7
        )
        button4.set_command(lambda: [print('button that deletes itself'), button4.close()])

        ###########
        # TOGGLES #
        ###########

        # a bunch of different toggles
        toggle1 = ui.Toggle(
            self,
            (25, button3.bottom + 25),
            25,
            ui.Pointer(True),
            border_thickness=4,
            corner_radius=0
        )

        toggle2 = ui.Toggle(
            self,
            (toggle1.right + 10, toggle1.top),
            25,
            ui.Pointer(False),
            border_thickness=4,
            corner_radius=7
        )

        toggle3 = ui.Toggle(
            self,
            (toggle2.right + 10, toggle1.top),
            25,
            ui.Pointer(True),
            border_thickness=4,
            corner_radius=-1
        )

        ##############
        # TEXT BOXES #
        ##############

        textbox1 = ui.Textbox(
            self,
            ui.Pointer('Yap here'),
            ('Nunito', 20),
            (25, toggle1.bottom + 20),
            (250, -1),
            padding=(7, 5),
            border_thickness=3,
            corner_radius=-1
        )

        textbox2 = ui.Textbox(
            self,
            ui.Pointer('No numbers, centered, tall'),
            ('Nunito', 20),
            (25, textbox1.bottom + 15),
            (350, 51),
            validation_function=lambda string: all(i not in string for i in '0123456789'), # numbers not allowed
            padding=(7, 5),
            border_thickness=3,
            corner_radius=-1,
            align_x='center'
        )

        ##########
        # IMAGES #
        ##########

        image = ui.Image(
            self,
            (25, textbox2.bottom + 20),
            'HRHS_logo.png',
            size=(400, 200)
        )

        #############
        # ALL PAGES #
        #############

        spacing_pages = 10
        padding_pages = (10, 5)
        border_thickness_pages = 3
        corner_radius_pages = -1

        pages_title = ui.Text(
            self,
            (1000, 25),
            'Pages',
            ('Nunito', 35, True, False)
        )

        accounts_button = ui.TextButton(
            self,
            'Accounts',
            ('Nunito', 25),
            (pages_title.left - 5, pages_title.bottom + spacing_pages),
            lambda: manager.go_to('accounts'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        add_bank_button = ui.TextButton(
            self,
            'Add Bank',
            ('Nunito', 25),
            (accounts_button.left, accounts_button.bottom + spacing_pages),
            lambda: manager.go_to('add_bank'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        add_expense_button = ui.TextButton(
            self,
            'Add Expense',
            ('Nunito', 25),
            (add_bank_button.left, add_bank_button.bottom + spacing_pages),
            lambda: manager.go_to('add_expense'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        add_income_button = ui.TextButton(
            self,
            'Add Income',
            ('Nunito', 25),
            (add_expense_button.left, add_expense_button.bottom + spacing_pages),
            lambda: manager.go_to('add_income'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        contact_button = ui.TextButton(
            self,
            'Contact',
            ('Nunito', 25),
            (add_income_button.left, add_income_button.bottom + spacing_pages),
            lambda: manager.go_to('contact'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        create_account_button = ui.TextButton(
            self,
            'Create Account',
            ('Nunito', 25),
            (contact_button.left, contact_button.bottom + spacing_pages),
            lambda: manager.go_to('create_account'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        faq_button = ui.TextButton(
            self,
            'FAQ',
            ('Nunito', 25),
            (create_account_button.left, create_account_button.bottom + spacing_pages),
            lambda: manager.go_to('faq'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        income_expenses_button = ui.TextButton(
            self,
            'Income & Expenses',
            ('Nunito', 25),
            (faq_button.left, faq_button.bottom + spacing_pages),
            lambda: manager.go_to('income_expenses'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        login_button = ui.TextButton(
            self,
            'Login',
            ('Nunito', 25),
            (income_expenses_button.left, income_expenses_button.bottom + spacing_pages),
            lambda: manager.go_to('login'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        more_button = ui.TextButton(
            self,
            'More',
            ('Nunito', 25),
            (login_button.left, login_button.bottom + spacing_pages),
            lambda: manager.go_to('more'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        settings_button = ui.TextButton(
            self,
            'Settings',
            ('Nunito', 25),
            (more_button.left, more_button.bottom + spacing_pages),
            lambda: manager.go_to('settings'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        snapshot_button = ui.TextButton(
            self,
            'Snapshot',
            ('Nunito', 25),
            (settings_button.left, settings_button.bottom + spacing_pages),
            lambda: manager.go_to('snapshot'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

        welcome_button = ui.TextButton(
            self,
            'Welcome',
            ('Nunito', 25),
            (snapshot_button.left, snapshot_button.bottom + spacing_pages),
            lambda: manager.go_to('welcome'),
            padding=padding_pages,
            border_thickness=border_thickness_pages,
            corner_radius=corner_radius_pages
        )

