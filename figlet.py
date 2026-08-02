import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]

    if font not in fonts:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

text = input("Input: ")

figlet.setFont(font=font)

print(figlet.renderText(text))

