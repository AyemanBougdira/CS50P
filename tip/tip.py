def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d2 = d.replace("$","")
    return float(d2)


def percent_to_float(p):
    p2 = p.replace("%", "")
    float(p2)
    return float(p2) / 100


main()
