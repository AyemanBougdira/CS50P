def main():
  text = input("entre ur text")
  convert(text)

def convert(text):
  text_modified = text.replace(":)", "🙂")
  text_modified2 = text_modified.replace(":(", "🙁")
  print(text_modified2)


main()
