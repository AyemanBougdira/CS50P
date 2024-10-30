names=[]

with open("names.txt", "r") as file:
  for line in file:
    names.append(line.rstrip())
  names.sort()

for name in names:
  print("hello", name)
