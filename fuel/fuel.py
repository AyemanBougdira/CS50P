def main():

  while True:
    Fraction = input("enter your fraction").strip().replace(" ", "")



    try:
      X , Y = Fraction.split("/")
      if int(X) > int(Y):
        continue
      percentage = (int(X)/int(Y))*100
      if percentage <= 1:
        print("E")
      elif percentage >= 99:
        print("F")
      else:
        print(f"{percentage:.0f}%")

    except ValueError:
      continue
    except ZeroDivisionError:
      continue
    else:
      break




main()
