def main():
  d = {
    "bajataco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "superburrito": 8.50,
    "superquesadilla": 9.50,
    "taco": 3.00,
    "tortillasalad": 8.00
}

  Total = 0
  while True:
    try:
      item = input("Choose your item:").strip().replace(" ", "").lower()
      if item not in d:
        continue
      else:
        Total += d[item]

    except EOFError:
      break

    print(f"${Total:.2f}")
main()
