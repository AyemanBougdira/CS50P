import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:  #opening and closing , "r" for readingn "w" for writting
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames = ["id" ,"english_title","japanese_title","brightness"]) #or fieldnames = reader.fieldnames + ["brightness"]
        writer.writeheader() # to write the header

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg") , 2)
            writer.writerow(row)

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

main()
