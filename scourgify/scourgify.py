import csv
import sys


def main():
    if verify_prompting():
        convert2name(sys.argv[1], sys.argv[2])


def convert2name(file1, file2):

    try:
        if verify_prompting():
            with open(f"{file1}" , "r") as input , open(f"{file2}", "w") as output:
                reader = csv.DictReader(input)
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames = fieldnames)
                writer.writeheader() #to write the header


                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first" : first,
                         "last" : last,
                         "house": row["house"]}
                    )



    except FileNotFoundError:
        sys.exit("File Not found")
    except ValueError as e:
        sys.exit(f"ValueError: {e}")
    except KeyError as e:
        sys.exit(f"KeyError: {e}")





def verify_prompting():

    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
         sys.exit("Too many command-line arguments")
    else:
        return True


main()
