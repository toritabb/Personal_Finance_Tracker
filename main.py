
# local
import ui
from constants import *
from ui import Window
from ui.event import event_manager
from ui.misc import Pointer



window = Window(SCREEN_SIZE)



########
# TEXT #
########

# normal, left align
text1 = ui.Text(
    window,
    (25, 25),
    'The quick brown fox\njumps over the lazy dog.',
    ('Nunito', 20),
    align = 'left'
)

# bold
text2 = ui.Text(
    window,
    (25, text1.bottom + 15),
    'The five boxing\nwizards jump quickly',
    ('Nunito', 20, True, False),
    align = 'center'
)

# italic
text3 = ui.Text(
    window,
    (25, text2.bottom + 15),
    'Jaded zombies acted\nquaintly but kept driving\ntheir oxen forward',
    ('Nunito', 20, False, True),
    align = 'right'
)

# bold and italic
text4 = ui.Text(
    window,
    (25, text3.bottom + 15),
    'Pack my box with five dozen liquor jugs.',
    ('Nunito', 20, True, True),
)

###########
# BUTTONS #
###########

# plain button
button1 = ui.Button(
    window,
    (25, text4.bottom + 25),
    (150, 40),
    lambda: print('button1'),
    border_thickness=5,
    corner_radius=10
)

# button with text and a fixed width but not height (the text ISN'T centered)
button2 = ui.TextButton(
    window,
    'TEST',
    ('Nunito', 30),
    (button1.right + 10, button1.top),
    (200, -1), # fixed width of 200, and height that adjusts to text size
    lambda: print('button2'),
    padding=10,
    border_thickness=0,
    corner_radius=-1 # corners automatically fully rounded
)

# button with text and padding (the text IS centered)
button3 = ui.TextButton(
    window,
    'Press Me!',
    ('Nunito', 20),
    (25, button1.bottom + 10),
    None,
    lambda: print('button3'),
    padding=(35, 7),
    border_thickness=0,
    corner_radius=-1
)

# button that deletes itself
button4 = ui.TextButton(
    window,
    'Delete',
    ('Nunito', 25),
    (button3.right + 10, button3.top),
    None,
    lambda: None,
    padding=7,
    border_thickness=2,
    corner_radius=7
)
button4.command = lambda: button4.close()

###########
# TOGGLES #
###########

# a bunch of different toggles
toggle1 = ui.Toggle(
    window,
    (25, button3.bottom + 25),
    25,
    Pointer(True),
    border_thickness=4,
    corner_radius=0
)

toggle2 = ui.Toggle(
    window,
    (toggle1.right + 10, toggle1.top),
    25,
    Pointer(False),
    border_thickness=4,
    corner_radius=7
)

toggle3 = ui.Toggle(
    window,
    (toggle2.right + 10, toggle1.top),
    25,
    Pointer(True),
    border_thickness=4,
    corner_radius=-1
)

toggle4 = ui.Toggle(
    window,
    (toggle1.left, toggle1.bottom + 10),
    25,
    Pointer(False),
    border_thickness=0,
    corner_radius=0
)

toggle5 = ui.Toggle(
    window,
    (toggle2.left, toggle4.top),
    25,
    Pointer(True),
    border_thickness=0,
    corner_radius=7
)

toggle6 = ui.Toggle(
    window,
    (toggle3.left, toggle4.top),
    25,
    Pointer(False),
    border_thickness=0,
    corner_radius=-1
)

##############
# TEXT BOXES #
##############

# basic text box
text_ptr = Pointer('Yap here')

textbox = ui.Textbox(
    window,
    text_ptr,
    ('Nunito', 20),
    (25, toggle6.bottom + 25),
    (250, -1),
    padding=(7, 5),
    border_thickness=3,
    corner_radius=-1
)



# main loop
while event_manager.running:
    event_manager.update()

    window.render()



# clean up
window.close()

