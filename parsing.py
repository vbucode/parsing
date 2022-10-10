import requests
url = "https://www.youtube.com"
r = requests.get(url)
html = r.text
with open("youtube.html", "a") as file:
    file.write(html)
