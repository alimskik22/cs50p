import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=f8afa5a387d52d34cd0c6cda22bbf1e977c594bedd4a23629fc41bf0b3df394d"
    )
except requests.RequestException:
    sys.exit()

data = response.json()

price = float(data["data"]["priceUsd"])
amount = n * price

print(f"${amount:,.4f}")
