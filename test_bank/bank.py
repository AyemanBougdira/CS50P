

def main():
    greeting = input("Whats your greeting").strip()
    print(value(greeting))


def value(greeting):
    if greeting[:5].lower().replace(" ", "") == "hello":
        return "$0"
    elif greeting[:1].lower().replace(" ", "")  == "h":
        return "$20"
    else :
        return "$100"


if __name__ == "__main__":
    main()
