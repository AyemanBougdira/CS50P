def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
  # Uppercase letters
  L= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  # Numbers
  N = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  if len(s) <= 1 or len(s) > 6 :
    return False
  if 2<= len(s) <=6:
    if s[0] not in L and s[1] not in L:
      return False
    for c in s:
      if c in L:
        if not s.index(c) == 5:
          if s[s.index(c) + 1] == "0" :
            return False

    for c in s:
      if c not in L and c not in N:
        return False
      elif s[s.index(c)] in N:
        for c in s[(s.index(c)+1):]:
          if c in L:
            return False
  return True

if __name__ == "__main__":
    main()
