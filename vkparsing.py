import requests
url = "https://x"
r = requests.get(url) #url - ссылка
html = r.text
f = open('x.html', 'w')
f.write(html)
f.close()
