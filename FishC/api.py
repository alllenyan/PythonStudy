import requests
import json

hosts = "https://dwz.cn"
path = "/admin/v2/create"

url = hosts + path
method = "post"
content_type = "application/json"

token = "1df2c83d9c46f9f86398dbbb062deb43"

bodys = {"Url":"http://www.baidu.com","TermOfValidity":"long-term"}

headers = {"Content_type":content_type,"token":token}

# response = requests.post(url=url,data=json.dumps(bodys),headers=headers)

response = requests.request(method,url=url,data=json.dumps(bodys),headers=headers)

print(response.text)