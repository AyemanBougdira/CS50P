import requests
import sys
import json

try:
  number = float(sys.argv[1])
except ValueError:
  sys.exit("Command-line argument is not a number")
except:
  if len(sys.argv) < 1:
    print("Missing Command-line argument")
    sys.exit()
  elif not sys.argv[1].isdigit():
    print("Command-line argument is not a number")
    sys.exit()
  else:
    print("Invalid Command-line argument")
    sys.exit()

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#print(json.dumps(response.json(), indent=2))
o = response.json()
o1 = o["bpi"]
o2 = o1["USD"]
amount = float(o2["rate_float"])*float(sys.argv[1])
print(f"${amount:,.4f}")

