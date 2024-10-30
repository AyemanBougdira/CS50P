import random

while True:
  try:
    n = int(input("Level:"))
    if n <= 0:
            raise ValueError()
  except ValueError:
        continue




  if n > 1:
    g = random.randint(1,n)


    while True:
      try:
         guess = int(input("Guess:"))
         if guess <=0:
            raise ValueError()
      except ValueError:
         continue

      if guess > g:
        print("Too large!")
        continue

      elif guess < g:
        print("Too small!")
        continue
      elif guess == g:
        print("Just right!")
        break
    break






