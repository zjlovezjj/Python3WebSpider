import requests
headers={
'cookie': 'd_c0="AKCmYOgvxA2PTuSo3wbQkD8qHhrgcI0gCig=|1529284195"; q_c1=74c33c93ad9445b5a5958176b3c1e4c6|1529284195000|1529284195000; _zap=4c9d1a11-ce20-4017-8193-ddec70f49c3a; capsion_ticket="2|1:0|10:1530178786|14:capsion_ticket|44:MTYwMjVlYjQyZmMxNDdlM2FmZjkyMmViMWU4ZTUxNTY=|b7fbab7d52b54ac2b5a5e5bab7f8e8d164df354c8d52d4f566d650e23b3451d2"; z_c0="2|1:0|10:1530178842|4:z_c0|92:Mi4xbVlXZkNnQUFBQUFBb0taZzZDX0VEU1lBQUFCZ0FsVk5HdnNoWEFENk1UcWFzMVlrNWhfa1lhbndLWFZnMXVjMVdR|74223f64e10b8bca1ee115dad4a60863dbb78be2423076e087274bb88b314154"; tgw_l7_route=8605c5a961285724a313ad9c1bbbc186; _xsrf=34b4d0c2-d420-4644-826e-b0a3884042b8; __utma=51854390.1264179408.1530417232.1530417232.1530417232.1; __utmb=51854390.0.10.1530417232; __utmc=51854390; __utmz=51854390.1530417232.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20180628=1^3=entry_date=20180618=1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
}
r=requests.get('https://www.zhihu.com',headers=headers)
with open('zhihu.html','wb') as f:
    f.write(r.content)