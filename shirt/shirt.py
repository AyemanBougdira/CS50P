import sys
import PIL
from PIL import Image
from PIL import ImageOps


def main():
    if verify_prompting():
          convertImage(sys.argv[1],sys.argv[2])


def verify_prompting():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 3:
        input_ext = sys.argv[1].lower().endswith(("jpg", "jpeg", "png"))
        output_ext = sys.argv[2].lower().endswith(("jpg", "jpeg", "png"))

        if not input_ext:
             sys.exit("Invalid input")
        elif not output_ext:
             sys.exit("Invalid output")
        elif sys.argv[1].split('.')[-1].lower() != sys.argv[2].split('.')[-1].lower():
             sys.exit("Input and output have different extensions")

    return True

def convertImage(imgg1, imgg2):
      with Image.open(imgg1) as background:
           foreground = Image.open("shirt.png")
           size = foreground.size
           fit = ImageOps.fit(background, size)
           fit.paste(foreground, foreground)
           fit.save(imgg2)



main()
