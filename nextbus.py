from textbitmaps import bitmaps
from papirus import Papirus
from PIL import Image
import time
import datetime
import predictions

SCREEN = Papirus()
SCREEN.update()

def display(s, full = False):
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
   i += 1
   now = datetime.datetime.now().strftime('%-I:%M:%S %p')
   preds = predictions.request_predictions()
   route_lines = '\n'.join(['  %s: %s' % (line, ', '.join(times)) for line, times in preds.items()])
   buffer = '%s\n%s\n%s' % ('        %s' % now, '  NextBus', route_lines)
   display(buffer, full=i % 3 == 0)
   time.sleep(10)
