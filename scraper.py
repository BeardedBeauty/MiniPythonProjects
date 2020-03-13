import requests
from bs4 import BeautifulSoup

q = requests.get("https://weather.com/weather/today/l/55347:4:US")
w = BeautifulSoup(q.content, "html.parser").find(id="LookingAhead")

r = []
y = w.find(classname="today-daypart-content")
for t in y:
    print(t)
    # r.append(y[t])


# print(w.find(class="today-daypart-temp")

# e = {
#     "today": {
#         "highlow": w.find(id="dp0-highLow")
#         "Ftemp": w.find(class="today-daypart-temp").find("span")
#     },
#     "tomorrow": w.find(),

# }
