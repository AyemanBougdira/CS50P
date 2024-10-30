

def main():
  expression = input("entre ur formula")
  x , y , z = expression.split(' ')


  if not ( y == "+" or y == "-" or y == "*" or y == "/"):
    print("Invalid operator")
    return

  if not ( x.isdigit() and z.isdigit()):
    print("Invalid input")
    return



  if y =="+":
    R = int(x) + int(z)
    print(f"{R:.1f}")
  elif y == "-":
    R = int(x) - int(z)
    print(f"{R:.1f}")
  elif y == "*":
    R = int(x) * int(z)
    print(f"{R:.1f}")
  elif y == "/":
    if z != 0:
      R = int(x) / int(z)
      print(f"{R:.1f}")

    else:
      print("Invalid input")
      return
  else:
    print("Invalid input")
    return



main()
