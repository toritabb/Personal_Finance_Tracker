
# local
import ui
from constants import *
from ui import Window
from ui.event import event_manager
from ui.misc import Pointer



window = Window(SCREEN_SIZE, True)

phrase = 'The quick brown fox jumped over the lazy dog.'

# normal
text1 = ui.Text(
    window,
    (25, 25),
    phrase,
    ('Nunito', 20)
)

# bold
text2 = ui.Text(
    window,
    (25, text1.bottom + 10),
    phrase,
    ('Nunito', 20, True, False)
)

# italic
text3 = ui.Text(
    window,
    (25, text2.bottom + 10),
    phrase,
    ('Nunito', 20, False, True)
)

# bold and italic
text4 = ui.Text(
    window,
    (25, text3.bottom + 10),
    phrase,
    ('Nunito', 20, True, True)
)

# plain button
button1 = ui.Button(
    window,
    (25, text4.bottom + 10),
    (250, 30),
    lambda: print('pressed'),
    border_thickness=2,
    corner_radius=10
)

# button with text (and adjustable padding)
button2 = ui.TextButton(
    window,
    'Press Me!',
    ('Nunito', 20),
    (25, button1.bottom + 10),
    None,
    lambda: print('Hi :)'),
    padding=(35, 7),
    border_thickness=0,
    corner_radius=-1
)

# button that deletes itself
button3 = ui.TextButton(
    window,
    'Delete',
    ('Nunito', 25),
    (button2.right + 10, button2.top),
    None,
    lambda: None,
    padding=10,
    border_thickness=2,
    corner_radius=5
)
button3.command = lambda: button3.close()

# a bunch of different toggles
toggle1 = ui.Toggle(
    window,
    (25, button2.bottom + 10),
    25,
    Pointer(True),
    border_thickness=5,
    corner_radius=0
)

toggle2 = ui.Toggle(
    window,
    (toggle1.right + 10, toggle1.top),
    25,
    Pointer(True),
    border_thickness=5,
    corner_radius=7
)

toggle3 = ui.Toggle(
    window,
    (toggle2.right + 10, toggle1.top),
    25,
    Pointer(True),
    border_thickness=5,
    corner_radius=-1
)

toggle4 = ui.Toggle(
    window,
    (toggle1.left, toggle1.bottom + 10),
    25,
    Pointer(True),
    border_thickness=3,
    corner_radius=0
)

toggle5 = ui.Toggle(
    window,
    (toggle2.left, toggle2.bottom + 10),
    25,
    Pointer(True),
    border_thickness=3,
    corner_radius=7
)

toggle6 = ui.Toggle(
    window,
    (toggle3.left, toggle3.bottom + 10),
    25,
    Pointer(True),
    border_thickness=3,
    corner_radius=-1
)



# main loop
while event_manager.running:
    event_manager.update()

    window.render()



# clean up
window.close()

