from bs4 import BeautifulSoup
import requests

headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
}
print("Enter search term: ", end='')
search = input()

param = {
    "q": search ,
    "hl": "en" , 
    "gl": "us" ,
    "lr": "lang_en"
    }
url = "https://www.google.com/search?"
r= requests.get(url, params=param, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("div", {"id": "main"})
#filesw = open("google_search.html", "w+", encoding="utf-8")
#filesw.write(str(results))
#results = soup.find("div", {"class": "eqAnXb"})
links = results.find_all("div", {"class": "egMi0 kCrYT"})
#print(str(links))
#links = results.findAll("a", "href")

for item in links:
    item_text = item.find("div").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href,"\n")