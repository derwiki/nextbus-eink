from textbitmaps import bitmaps
from papirus import Papirus
from PIL import Image
import time
import datetime
import predictions


SCREEN = Papirus()
SCREEN.update()


def display(s, full=False):
    img, _ = bitmaps.display_text_prop(s, display_size=(200, 96), char_size=2)
    img.save("tmp.bmp")
    file = Image.open("tmp.bmp")
    SCREEN.display(file)
    if full:
        SCREEN.update()
    else:
        SCREEN.partial_update()


i = 0
while True:
    try:
        current_predictions = predictions.request_predictions()
        i += 1
        now = datetime.datetime.now().strftime('%-I:%M:%S %p')
        buffer = '\n'.join((
            '        {}'.format(now),
            '  NextBus',
            '  10: {}, {}'.format(*current_predictions['10']),
            '  48: {}, {}'.format(*current_predictions['48']),
        ))
        display(buffer, full=i % 3 == 0)
    except Exception as e:
        print(str(e))

    time.sleep(10)
