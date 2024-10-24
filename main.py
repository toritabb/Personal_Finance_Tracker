import random

# local
import ui
from constants import *
from ui import Window
from ui.event import event_manager



window = Window(SCREEN_SIZE, True)

phrase = 'The quick brown fox jumped over the lazy dog.'

text1 = ui.Text(
    window,
    (25, 25),
    phrase,
    ('Inter', 20, True, False)
)

text2 = ui.Text(
    window,
    (25, text1.bottom + 10),
    phrase,
    ('Lexend', 20, True, False)
)

text3 = ui.Text(
    window,
    (25, text2.bottom + 10),
    phrase,
    ('Eater', 20, False, True)
)

button1 = ui.Button(
    window,
    (25, text3.bottom + 10),
    (250, 30),
    lambda: print('pressed'),
    border_thickness=3,
    corner_radius=10
)
button2 = ui.TextButton(
    window,
    'Press Me!',
    ('Lexend', 20, False, False),
    (25, button1.bottom + 10),
    None,
    lambda: print('Hi :)'),
    padding=5,
    border_thickness=0,
    corner_radius=30
)
button3 = ui.TextButton(
    window,
    'Delete',
    ('Eater', 25, False, False),
    (25, button2.bottom + 10),
    None,
    lambda: None,
    padding=2,
    border_thickness=5,
    corner_radius=10
)

button3.command = lambda: random.choice((text1.close, text2.close, text3.close, button1.close, button2.close, button3.close))()



while event_manager.running:
    event_manager.update()

    window.render()



window.close()
