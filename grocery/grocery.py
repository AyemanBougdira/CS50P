def main():

  d = {}
  while True:

    try:
      item = input()
      if item in d:
        d[item] += 1
      else:
        d[item] = 1
    except EOFError:
      break


  dictionnaire_trie = {clé: d[clé] for clé in sorted(d)}

  for k, v in dictionnaire_trie.items():
    print(v, k.upper(), end = "\n")


main()
