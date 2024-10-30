
L = []
while True:

  try:
    name = input("entre a name")
    L.append(name)
  except EOFError:
    break

n = len(L)
str ="Adieu, adieu, to "

while True:
    if n == 1:
        print(str + L[0])
        break

    if n == 2:
        print(str + L[0] + " and " + L[1] )
        break

    else:
        for i in range(n-1):
            str += L[i] + "," + " "

        str = str + "and " + L[-1]

        print(str)
        break
