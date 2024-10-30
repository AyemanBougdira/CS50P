import csv
import sys

from tabulate import tabulate




def main():

    if verify_prompting():
        print(csv_to_table(sys.argv[1]))



def verify_prompting():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
        return False
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
        return False
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
        return False
    else:
        return True


def csv_to_table(filename):

        try:
            with open(f"{filename}", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
        except FileNotFoundError:
            sys.exit("File does not exist")


main()
