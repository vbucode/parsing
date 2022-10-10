import requests
url = "https://youtube.com"
r = requests.get(url)
html = r.text
f = open('youtube.html', 'w')
f.write(html)
f.close()
