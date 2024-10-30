def main():


  Input = input("entre your input")
  L = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
  Output = ""
  for c in Input:
    if not c in L:
      Output += c
  print(Output)

main()
