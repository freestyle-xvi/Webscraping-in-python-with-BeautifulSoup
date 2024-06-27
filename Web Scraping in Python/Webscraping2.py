from bs4 import BeautifulSoup
import re

#uses index2.html 

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
    
result = doc.find("option") # finds only one iteration of the operation tag
results = doc.find_all("option")  # finds all iterations of the operation tag

# tags = doc.find_all(["option"],text="Undergraduate", value="undergraduate") # finds multiple texts and values that contain the word undergraduate

#tags = doc.find_all(class_="btn-item") # finds a specific class in the html document

# tags = doc.find_all(text=re.compile("\$."), limit=1) # limit keyword limits results 

tags = doc.find_all(input, type="text")
for tags in tags:
    tags['placeholder'] = "Tag has been changed here!"
    
with open("changed.html", "w") as file:
    file.write(str(doc))

# for tags in tags:
#    print(tags.strip())
