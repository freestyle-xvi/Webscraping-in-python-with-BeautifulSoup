from bs4 import BeautifulSoup
import requests
import re

#WORK IN PROGRESS 2/5 WEBSITES PROPERLY WORKING FOR DATA TO BE SCRAPED AS OF 27/06/2024

gpu = input("What product are you searching for? ")

urls = {
    "Newegg": "https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48",
    "Wootware": "https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby/in_stock_with_wootware",
    "Takealot": "https://www.takealot.com/computers/graphics-cards-26421?sort=ReleaseDate%20Descending",
    "Evetech": "https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx",
    "Dreamware Tech": "https://www.dreamwaretech.co.za/c/computer-components/graphics-cards-gpus/nvidia-graphics-cards/"
}

products = []

for site_name, url in urls.items():
    try:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')
        
        print(f"Scraping {site_name} ({url})")
        
        if site_name == "Newegg":
            items = soup.find_all('div', class_='item-cell')
            for item in items:
                title = item.find('a', class_='item-title')
                price = item.find('li', class_='price-current')
                if title and price and re.search(gpu, title.text, re.I):
                    products.append([title.text.strip(), price.text.strip(), site_name])
                    
        elif site_name == "Wootware":
            items = soup.find_all('div', class_='main-info')
            for item in items:
                title = item.find('h2', class_='product-name')
                price = item.find('span', class_='price')
                if title and price and re.search(gpu, title.text, re.I):
                    products.append([title.text.strip(), price.text.strip(), site_name])
        
        
        #commented out as tags are still to be prorperly targeted to aquire the specif required info (sa websites suck :/ )
        #-----------------------------
        # elif site_name == "Takealot":
        #     items = soup.find_all('a', class_='product-anchor product-card-module_product-anchor_TUCBV')
        # for item in items:
        #     title = item.find('h4', class_='product-title')
        #     price_container = item.find('div', class_='product-card-module_price-wrapper_2waB1')
        #     price = price_container.find('li', class_='price product-card-module_price_zVU6d')  # Target nested price element
        #     if title and price and "4060" in title.text.strip():
        #         # Extract price text
        #         price_text = price.find('span', class_='currency plus currency-module_currency_29IIm').text.strip()  # Extract price text within the currency span
        #         products.append([title.text.strip(), price_text, site_name])
           
        # elif site_name == "Evetech":
        #     items = soup.find_all('div', class_='ComponentCard_Products__Card__eusjG ComponentCard_HoverGrow__TVW8j shadow overflow-hidden h-100 gap-2 position-relative card')
        #     for item in items:
        #         title = item.find('h3', class_='fs-6 fw-2 lh-1 m-0 overflow-hidden h-100')
        #         price = item.find('div', class_='ComponentCard_Products__Price__f5994 fw-3 fs-3 flex-shrink-0')
        #         if title and price and re.search(gpu, title.text, re.I):
        #             products.append([title.text.strip(), price.text.strip(), site_name])
                    
        #         elif site_name == "DreamwareTech":
        #              items = soup.find_all('div', class_='product-details')
        #         for item in items:
        #             title = item.find('h2', class_='product-name')
        #             price = item.find('div', class_='product-price')
        #             if title and price and re.search(gpu, title.text, re.I):
        #                 products.append([title.text.strip(), price.text.strip(), site_name])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

#  results in a simple table format
print("\n" + "-" * 75)
print(f"{'Product Name':<50} {'Price':<15} {'Store':<10}")
print("-" * 75)

for product in products:
    print(f"{product[0]:<50} {product[1]:<15} {product[2]:<10}")

print("-" * 75)
