from bs4 import BeautifulSoup

import requests

url = "https://www.newegg.com/msi-geforce-rtx-4060-rtx-4060-ventus-2x-white-8g-oc/p/N82E16814137832" 

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

price = doc.find_all(text="$")
parent = price[0].parent # shows the entire tag (parent tag) which encases where the price is stored
    
#searching for the price within the parent tag
strong = parent.find("strong")
print(strong.text) # prints the price only of the rtx 4060 from neweggs site



#beautifulsoup uses a tree type structure to read through elements of the html page for example the tag then the content of the tag