# data is taken from https://coinmarketcap.com

from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

DataTable = doc.tbody # parent tag
trs = DataTable.contents #sibling tag

#print(trs[0].next_sibling) # prints second element in table prints all html code

# print(list(trs[0].next_siblings)) # prints every row in the table after first element

#print(trs[0].parent) # prints entire table within the tbody tag

#print(trs[0].parent.name) # prints the name of the parent tag

#print(list(trs[0].descendants)) # prints everything after or inside of the tag


# printing and formatting of the first 10 names and prices of the data
prices = {}

for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string.strip()  # Remove any extra whitespace
    fixed_price = price.span.string.strip()  # Remove any extra whitespace

    prices[fixed_name] = fixed_price

# Printing the heading
print(f"{'Name of Cryptocurrency':<30} {'Price':>10}")
print("="*40)

# Printing the name and price in a tabular format
for name, price in prices.items():
    print(f"{name:<30} {price:>10}")

