def main():

  cost = 50
  total = 0
  L = [25, 10, 5]

  while total < 50:
    coin = int((input("entre a coin")))
    if coin in L:
      total +=coin
      print("Amount Due:", cost - total)
    else:
      print("Amount Due:", 50)
  print("Change Owed:", total - cost)

main()
