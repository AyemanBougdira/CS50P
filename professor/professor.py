import random

def main():
    level = get_level()
    Score = 0
    for i in range(10):
        X, Y = generate_integer(level)
        Z = int(input((f"{X} + {Y} = ")))
        if X + Y == Z :
            Score = Score + 1
            continue
        else:
            print("EEE")
            for _ in range(2):
                Z = int(input((f"{X} + {Y} = ")))
                if X + Y == Z :
                    Score = Score + 1
                    break
            if Z != X + Y:
                print(f"{X} + {Y} =", X + Y)




    print("Score:", Score)


def get_level():
    while True:
        try:
            level = int(input("entre ur level"))
            if level not in [1,2,3]:
                raise ValueError
            else:
                break

        except ValueError:
            continue
    return level


def generate_integer(level):
    if level == 1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
        return X, Y
    elif level == 2:
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
        return X, Y
    elif level == 3:
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
        return X, Y




if __name__ == "__main__":
    main()
