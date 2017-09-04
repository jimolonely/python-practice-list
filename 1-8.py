#!/usr/bin/env python
#-*-coding:utf-8-*-

import time
import sys

class ProgressBar():
    '''
     进度条
    '''
    i = 1 # 当前进度
    step = 1 # 每步大小
    max_len = 60 # 进度条长度
    max_num = 0 # 进度条总步数
    
    def __init__(self,max_num,max_len=100):
        self.max_num = max_num
        self.max_len = max_len
        self.i = 1
        self.step = 1

    def process(self,i=None,step=None):
        if i is not None:
            self.i = i
        if step is not None:
            self.step = step
        now_len = int(self.i/self.max_num*self.max_len) #已处理长度
        rest_len = self.max_len - now_len #待处理长度
        percent = self.i * 100.0 / self.max_num
        bar = '['+'*'*now_len+'-'*rest_len+']'\
              +'%.2f'%percent+'%\r' # \r表示不换行且回到行首
        sys.stdout.write(bar)
        sys.stdout.flush()
        self.i += self.step

    def finish(self,msg='Done'):
        print('')
        print(msg)
        self.i = 1
        self.step = 1

def download(max_num=100,step=1):
    bar = ProgressBar(max_num)
    for i in range(0,max_num+step,step):
        bar.process(i=i)
        time.sleep(0.02)
    bar.finish()

if __name__=='__main__':
    download()
    download(1000,5)
    
    
        
