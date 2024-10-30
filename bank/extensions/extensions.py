def main():
  File_name = input("Whats your File name").strip()
  if File_name[-4:].lower().replace(" ", "") == ".gif" :
    print("image/gif")
  elif File_name[-4:].lower().replace(" ", "") == ".jpg" :
    print("image/jpeg")
  elif File_name[-4:].lower().replace(" ", "") == ".png" :
    print("image/png")
  elif File_name[-4:].lower().replace(" ", "") == ".pdf" :
    print("application/pdf")
  elif File_name[-4:].lower().replace(" ", "") == ".txt" :
    new = File_name.lower().replace(".txt", "")
    print(f"text/{new}")
  elif File_name[-4:].lower().replace("", "") == ".zip" :
    print("application/zip")
  elif File_name[-4:].lower().replace(" ", "") == ".bin" :
    print("application/octet-stream")
  elif File_name[-5:].lower().replace(" ", "") == ".jpeg" :
    print("image/jpeg")
  else:
    print("application/octet-stream")


main()
  