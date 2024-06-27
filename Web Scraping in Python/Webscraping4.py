from bs4 import BeautifulSoup
import requests
import re

def get_total_pages(search_term):
    """Retrieve the total number of pages for the search term."""
    url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    page_text = doc.find(class_="list-tool-pagination-text")
    
    if page_text:
        pages = int(str(page_text.strong).split("/")[-2].split(">")[-1][:-1])
        return pages
    return 1

def scrape_newegg(search_term, pages):
    """Scrape Newegg for the given search term across the specified number of pages."""
    items_found = {}
    
    for page in range(1, pages + 1):
        url = f"https://www.newegg.com/p/pl?d={search_term}&N=4131&page={page}"
        page = requests.get(url).text
        doc = BeautifulSoup(page, "html.parser")

        div = doc.find(class_="item-cells-wrap border-cells short-video-box items-grid-view four-cells expulsion-one-cell")
        if not div:
            continue
        
        items = div.find_all(text=re.compile(search_term, re.IGNORECASE))
        
        for item in items:
            parent = item.parent
            if parent.name != "a":
                continue

            link = parent['href']
            next_parent = item.find_parent(class_="item-container")
            if not next_parent:
                continue
            
            try:
                price = next_parent.find(class_="price-current").find("strong").string
                if not price:
                    price = next_parent.find(class_="price-current").find("sup").string
                items_found[item] = {"price": int(price.replace(",", "")), "link": link}
            except AttributeError:
                continue

    return items_found

def main():
    search_term = input("What product are you searching for? ")
    pages = get_total_pages(search_term)
    items_found = scrape_newegg(search_term, pages)
    
    sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

    for item in sorted_items:
        print(item[0])
        print(f"${item[1]['price']}")
        print(item[1]['link'])
        print("-------------------------------")

if __name__ == "__main__":
    main()
