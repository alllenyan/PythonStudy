import requests
import bs4

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

res = requests.get("https://movie.douban.com/top250",headers = headers)

soup = bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_='hd')

for each in targets:
    print(each.a.span.text)