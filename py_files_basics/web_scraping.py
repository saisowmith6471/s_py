import requests
import bs4

content = requests.get("https://en.wikipedia.org/wiki/Electric_car")
print(content.text)
soup = bs4.BeautifulSoup(content.text)
print(soup)
x = soup.select_one("#mw-content-text")
print(x)










