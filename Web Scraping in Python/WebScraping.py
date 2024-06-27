from bs4 import BeautifulSoup

with open("index.html") as f :
    doc = BeautifulSoup(f, "html.parser")
    
    
#print(doc.prettify)

tag = doc.title
tag.string = "Fujifilm or Panasonic cameras for travel" #getting the content of the tag with the .string

tags = doc.find_all("p")[0] # finding all content that are in between the p tag

print(tags.find_all("b"))