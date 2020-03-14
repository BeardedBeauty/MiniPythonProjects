import requests
from bs4 import BeautifulSoup
import re

q = requests.get("https://weather.com/weather/today/l/55347:4:US")
w = BeautifulSoup(q.content, "html.parser").find(id="LookingAhead")
y = w.find(class_="today-daypart-content")
e = re.search("[0-9]+", str(y.find(class_="")))
r = re.search(">High<|>Low<", str(y.find(id="dp0-highLow")))
r = r.group().replace("<", "")
r = r.replace(">", "")


class Day:
    def __init__(d, days, temp, lh):
        d.days = days
        d.temp = temp
        d.lh = lh


today = Day("today", e.group(), r)
print(today.days + today.temp + today.lh)
