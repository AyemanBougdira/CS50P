

def main():
    Input = input("entre your input")
    print(shorten(Input))



def shorten(word):
    L = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    Output = ""
    for c in word:
        if not c in L:
            Output += c
    return Output


if __name__ == "__main__":
    main()
