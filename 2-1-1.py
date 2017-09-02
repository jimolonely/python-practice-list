#!/usr/bin/env python
#-*-coding:utf-8-*-

import urllib2

def access_by_proxy(url,proxy_ip):
    # agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
    proxy_support = urllib2.ProxyHandler({"http":proxy_ip})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    content = urllib2.urlopen(url)
    return content

if __name__=='__main__':
    url = 'http://www.baidu.com'
    proxy_ip = '220.189.249.80:80'
    try:
        content = access_by_proxy(url,proxy_ip)
        print(content.info()) #打印头部信息
    except:
        print('err')