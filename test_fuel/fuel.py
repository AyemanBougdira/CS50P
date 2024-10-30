def main():
    fraction = input("Enter your fraction: ").strip().replace(" ", "")
    try:
        percentage = convert(fraction)
        print(gauge(percentage))
    except (ValueError, ZeroDivisionError):
        print("Invalid fraction. Please try again.")


def convert(fraction):
    try:
        X, Y = fraction.split("/")
        X = int(X)
        Y = int(Y)

        if Y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if X > Y:
            raise ValueError("Numerator cannot be greater than the denominator.")

        percentage = (X / Y) * 100
        return percentage

    except ValueError:
        raise ValueError("Invalid input. Please enter a valid fraction in the form 'X/Y'.")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
