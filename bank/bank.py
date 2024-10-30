def main():
  greeting = input("Whats your greeting").strip()
  if greeting[:5].lower().replace(" ", "") == "hello":
    print("$0")
  elif greeting[:1].lower().replace(" ", "")  == "h":
    print("$20")
  else :
    print("$100")

main()
