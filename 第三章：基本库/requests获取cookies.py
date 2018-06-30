import requests
r=requests.get('https://www.baidu.com')
print(r.cookies)
for key,item in r.cookies.items():
    print(key+'='+item)