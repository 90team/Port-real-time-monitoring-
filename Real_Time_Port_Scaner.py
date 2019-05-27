# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:秋某人的傻逼                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量URL_Fuzz检测工具        *
#*********************************************

#--------------------/工具编写思路/--------------------
#1.定义定时扫描功能 bat脚本实现
#2.对扫描结果导出含有日期 实现
#3.设置邮件系统 实现
#4.定时发送邮件 定时扫描功能结合
#--------------------/工具编写思路/--------------------
import socket
import time
import mail_send
import os
import threading
import dir_creater
import datetime
import judge
import finderrorport

#---------------------------//定义父类 线程
class myThread (threading.Thread):
    #----------------------//实例化
    def __init__(self, threadID, start_num, end_num):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.start_num = start_num
        self.end_num = end_num
    #-------------//启动线程
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        get_ip_status(self.threadID, self.start_num, self.end_num)
        # 释放锁，开启下一个线程
        threadLock.release()

def get_ip_status(id,start,end):
    print ('进程ID：'+ str(id))
    # 定义要创建的目录
    dir_nowtime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    mkpath = dir_nowtime
    dir_creater.mkdir(mkpath)
    for ip in open('hosts.txt','r'):
        for port in range(start,end):
            timeout = 0.1
            socket.setdefaulttimeout(timeout)  # 这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                server.connect((ip,port))
                print('{0} port {1} is open'.format(ip.strip(), port))
                nowtime = time.strftime("%Y-%m-%d")
                text_path = dir_nowtime + '/' + ip.replace('.','_').strip() + '-' + nowtime + '.txt'
                with open(text_path,'w') as f:
                    f.writelines('{0} port {1} is open'.format(ip.strip(), port))
                    f.writelines('\n')
            except Exception as e:
                print (('{0} port {1} is close'.format(ip.strip(), port)),'|','失败原因：',e)
            finally:
                server.close()
    #获取最新文件
    #file_dict = {}
    lists = os.listdir(dir_nowtime)  # 先获取文件夹内的所有文件
    mail_value_list = []
    for i in lists:  # 遍历所有文件
        if os.path.splitext(i)[1] == '.txt':
            print(i)
            txtname = os.path.splitext(i)[0]
            # ctime = os.stat(os.path.join('/', i)).st_ctime
            # file_dict[ctime] = i  # 添加创建时间和文件名到字典
            # max_ctime = max(file_dict.keys())  # 取值最大的时间
            # newfile_name = file_dict[max_ctime]  # 最新文件名
            with open(dir_nowtime + '/'+i, 'r') as f:
                mail_value = f.read().strip()
                mail_value_list.append(mail_value)
        else:
            print ('×')
    value_mail = str(mail_value_list)
    print (value_mail)
    value_mail_rep = value_mail.replace('.','_')
    value_mail_rep2 = value_mail_rep.replace(' ','')
    value_mail_rep3 = value_mail_rep2.replace('port','_')
    value_mail_rep4 = value_mail_rep3.replace('isopen','')
    print(value_mail_rep4,file=open(dir_nowtime + '/' +'result.txt','w+'))
    # mail_send.mail(value_mail + dir_nowtime)
    # judge.re_judge(value_mail_rep4)
    if len(value_mail) == 2:
        print ('列表值为空！')
    elif judge.re_judge(value_mail_rep4) == False:
        while mail_send.mail(value_mail + dir_nowtime) == False:
            finderrorport.fderror(dir_nowtime + '/' +'result.txt',value_mail_rep4)
            mail_send.mail(value_mail_rep4 + dir_nowtime)
        print('发送通知邮件成功！')
    else:
        print ('不存在异常端口，无需发送邮件提醒！')
threadLock = threading.Lock()
threads = []
if __name__ == '__main__':
    # 开始时间：
    starttime = datetime.datetime.now()
    # #创建新线程
    thread1 = myThread(1, 1, 32768)
    thread2 = myThread(2, 32768, 65536)
    #开启新线程
    thread1.start()
    thread2.start()
    #添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    #等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")
    #结束时间
    endtime = datetime.datetime.now()
    print (endtime - starttime)
    # pool = threadpool.ThreadPool(10)
    # for list in range(2,30000):
    #     print (list)
    #     for list2 in range(30001,65535):
    #         # 创建一个包含2条线程的线程池
    #         pool = ThreadPoolExecutor(max_workers=2)
    #         # 向线程池提交一个task, 50会作为get_ip_status()函数的参数
    #         future1 = pool.submit(get_ip_status, list)
    #         # 向线程池再提交一个task, 100会作为get_ip_status()函数的参数
    #         future2 = pool.submit(get_ip_status, list2)
    #         # 判断future1代表的任务是否结束
    #         print(future1.done())
    #         time.sleep(3)
    #         # 判断future2代表的任务是否结束
    #         print(future2.done())
    #         # 查看future1代表的任务返回的结果
    #         print(future1.result())
    #         # 查看future2代表的任务返回的结果
    #         print(future2.result())
    #         # 关闭线程池
    #         pool.shutdown()
    #requests = threadpool.makeRequests(get_ip_status,list_end)
    #[pool.putRequest(req) for req in requests]
    # 创建两个线程
    # get_ip_status()
    # timer = threading.Timer(10,get_ip_status)
    # timer.start()
    # 创建新线程
    # thread1 = myThread(1, 1, 65535)
    # thread2 = myThread(2, 200, 400)
    # 开启新线程
    # thread1.start()
    # thread2.start()
    # 添加线程到线程列表
    # threads.append(thread1)
    # threads.append(thread2)
    # 等待所有线程完成
    # for t in threads:
    #     t.join()
    # print("退出主线程")