import requests
from bs4 import BeautifulSoup

q = requests.get("https://weather.com/weather/today/l/55347:4:US")
w = BeautifulSoup(q.content, "html.parser").find(id="LookingAhead")

print(w.find(classname="today-daypart-content").find(class_="today-daypart-temp"))

# e = {
#     "today": {
#         "highlow": w.find(id="dp0-highLow")
#         "Ftemp": w.find(class="today-daypart-temp").find("span")
#     },
#     "tomorrow": w.find(),

# }
