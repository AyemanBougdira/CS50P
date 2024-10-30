def main():
  time = input("Enter time")
  hours, minutes = time.split(":")
  if not ( hours.isdigit() and minutes.isdigit()):
    print("Invalid input")
    return

  elif int(minutes) >= 60:
    print("Invalid input")
    return

  elif not ( 0 <= int(hours) < 24):
    print("Invalid input")
    return

  convert(time)
  if 7 <= convert(time) <= 8:
    print("breakfast time")
  elif 12 <= convert(time) <= 13:
    print("lunch time")
  elif 18 <= convert(time) <= 19:
    print("dinner time")




def convert(time):
  hours, minutes = time.split(":")
  minutes2 = int(minutes) / 60
  total_hours = int(hours) + minutes2
  return total_hours


if __name__ == "__main__":
    main()
