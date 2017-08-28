#-*-coding:utf-8-*-
'''
author:jackpler

'''
import time

class VideoTape():

    def __init__(self,name,day_price):
        self.name = str(name)
        self.day_price = float(day_price) # 每天借的费用
    
class Shop():

    # 模拟数据库表存数据
    '''
        {
            'user_id':-1,
            'video':'xxx',
            'from_time':23123,
            'day':0, # 借阅天数
            'cost':0
            'return_time':342121
            'overdue_cost':0.0 # 逾期费用
        }
    '''
    data = [
    ]

    '''
    从后往前找最近的记录
    '''
    @staticmethod
    def find_last_borrow_record(video_name,user_id):
        length = len(Shop.data)
        for i in range(length-1,-1,-1):
            d = Shop.data[i]
            if d['video']==video_name and d['user_id']==user_id:
                return i
        return -1

    '''
    用户id为空就查所有记录
    '''
    @staticmethod
    def show_record(user_id=None):
        if user_id==None:
            for d in Shop.data:
                # print(d)
                print('用户id=%d的用户在%s借阅影碟《%s》,于%s归还,总费用为：%.2f,逾期费用为%.2f'%\
                      (d['user_id'],time.strftime('%Y-%m-%d',time.localtime(d['from_time'])),\
                       d['video'],time.strftime('%Y-%m-%d',time.localtime(d['return_time'])),\
                       d['cost'],d['overdue_cost']))
                       
        else:
            pass


class User():
    id = 0 # 用户的自增id
    
    # 用户
    def __init__(self,name):
        self.name = name
        self.shop = None
        self.id = User.id
        User.id += 1

    # 借某个video多少天
    def borrow(self,video,day):
        price = video.day_price * day
        d = {}
        d['user_id'] = self.id
        d['video'] = video.name
        d['from_time'] = float(time.time())
        d['day'] = int(day)
        d['cost'] = float(price)
        d['return_time'] = 0.0
        d['overdue_cost'] = 0.0
        Shop.data.append(d)

    def remand(self,video):
        i = Shop.find_last_borrow_record(video.name,self.id)
        if i==-1:
            print('没有借的记录何来归还？')
            return
        # 更新归还时间，这里假设是7天后
        d = Shop.data[i]
        d['return_time'] = d['from_time'] + 24*7*3600
        len_day = (d['return_time'] - d['from_time'])/(3600*24)
        if len_day > d['day']:
            d['overdue_cost'] = (len_day - d['day'])*10 # 假设超期每天10元
        else :
            d['overdue_cost'] = 0.0

        
if __name__=='__main__':
    
    jimo = User('jimo')
    jack = User('jack')

    video1 = VideoTape('猫和老鼠',10.5)
    video2 = VideoTape('A计划',20)

    jimo.borrow(video1,10)
    jack.borrow(video1,5)
    jack.borrow(video2,8)

    jimo.remand(video1)
    jack.remand(video1)
    jack.remand(video2)

    Shop.show_record()
