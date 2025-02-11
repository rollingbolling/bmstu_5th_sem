import requests as re
import bs4

LIMIT = 200
FILE_URLS = "urls.txt"
URL = "https://1001retsept.ru"
CLASSES = [
    'vtemlevel1vtaccmenu02',
    'vtemlevel2vtaccmenu02',
    'vtemlevel3vtaccmenu02'
]
REC_CLASS = 's5_pagetitlewrap'

unique_urls = set()

def parse(class_name):
    page = re.get(URL)
    page.raise_for_status()

    bs = bs4.BeautifulSoup(page.text, 'html.parser')

    blocks = bs.find_all(class_ = class_name)
    for ctg in blocks:
        data = ctg.find_all('a')
        for cur_data in data:
            cur_url = URL + cur_data.get('href')
            
            page = re.get(cur_url)
            page.raise_for_status()
            
            bs = bs4.BeautifulSoup(page.text, 'html.parser')
            
            recepts = bs.find_all('div', class_ = REC_CLASS)
            
            for cur_rec in recepts:
                unique_urls.add(URL + cur_rec.find('a').get('href'))
                if len(unique_urls) >= LIMIT:
                    return unique_urls
    return unique_urls

def write_to_file():
    with open(FILE_URLS, 'w', encoding='utf-8') as file:
        for text in unique_urls:
            file.write(f"{text}\n")

if __name__ == "__main__":
    for class_name in CLASSES:
        if len(unique_urls) >= LIMIT:
            break
        parse(class_name)
        
    write_to_file()
    print("Done")
