import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) or not sys.argv[
    2
].lower().endswith((".jpg", ".jpeg", ".png")):
    sys.exit("Not an img file")
elif splitext(sys.argv[1])[1] != splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")
else:
    try:
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        before = ImageOps.fit(before, size)
        before.paste(shirt, shirt)
        before.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File not found")
