import urllib.request
response=urllib.request.urlopen('https://www.python.org')
print(response.getheaders()) #获取响应头
print(response.getheader('Server')) #获取响应头中的Server值