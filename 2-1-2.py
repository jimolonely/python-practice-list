#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests

def access_by_proxy(url,proxy_ips):
    html = requests.get(url,proxies=proxy_ips)
    return html

if __name__=='__main__':
    url = 'http://www.baidu.com'
    proxy_ip = {'http':'220.189.249.80:80'}
    try:
        html = access_by_proxy(url,proxy_ip)
        print(html.text) #打印页面信息
    except:
        print('err')