import requests

url = "http://www.baidu.com/s?"

headers  = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

pama = {
    "wd" : "python"
}

response = requests.get(url,headers=headers,params=pama)

print(response.content)
print(response.text)
print(response.encoding)

with open(r'C:\Users\Administrator\Desktop\bdsearch.html',"wb") as f:
    f.write(response.content)
