import requests
from bs4 import BeautifulSoup

q = requests.get("https://weather.com/weather/today/l/55347:4:US")
w = BeautifulSoup(q.content, "html.parser")

print(w)
