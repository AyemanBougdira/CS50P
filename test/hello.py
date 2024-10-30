

def main():
    Input = input("entre your input")
    shorten(Input)


def shorten(word):
    L = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    Output = ""
    for c in Input:
        if not c in L:
        Output += c


if __name__ == "__main__":
    main()
