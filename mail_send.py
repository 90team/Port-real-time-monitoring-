# -*- coding:UTF-8 -*-
#*********************************************
#------->>>>>>Author:##########                *
#------->>>>>>Name:熊猫最爱皮卡丘                 *
#------->>>>>>Target:批量URL_Fuzz检测工具        *
#*********************************************
#邮件服务器0
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# def mail(i,txtname):
#     try:
#         sender = 'hacker9090@126.com'
#         receiver = list()#接收者列表
#         receiver.append('2698392815@qq.com')
#         copyReceive = list()#抄送者列表
#         copyReceive.append(sender)#将发件人添加到抄送列表
#         username = 'hacker9090@126.com'#发件人邮箱账号
#         mailall=MIMEMultipart()
#         mailall['Subject'] = "[外网资产:"+ txtname +"]端口扫描结果" #记住一定要设置，并且要稍微正式点
#         mailall['From'] = sender #发件人邮箱
#         mailall['To'] = ';'.join(receiver) #收件人邮箱,不同收件人邮箱之间用;分割
#         mailall['CC'] = ';'.join(copyReceive)  #抄送邮箱
#         with open(i, 'r') as f:
#             mail_value = str(f.read()).encode()
#         mailcontent = mail_value
#         mailall.attach(MIMEText(mailcontent, 'plain', 'utf-8'))
#         mailAttach = '测试邮件附件内容'
#         contype = 'application/octet-stream'
#         maintype, subtype = contype.split('/', 1)
#         filename = '免责声明.txt'#附件文件所在路径
#         attfile = MIMEBase(maintype, subtype)
#         attfile.set_payload(open(filename, 'rb').read())
#         attfile.add_header('Content-Disposition', 'attachment',filename=('utf-8', '', filename))#必须加上第三个参数，用于格式化输出
#         mailall.attach(attfile)
#         fullmailtext = mailall.as_string()
#         smtp = smtplib.SMTP()
#         smtp.connect('smtp.126.com')
#         smtp.login(username, password)
#         smtp.sendmail(sender, receiver+copyReceive, fullmailtext)#发送的时候需要将收件人和抄送者全部添加到函数第二个参数里
#         smtp.quit()
#     except Exception as e:
#         print ('发送出错，内容是：',e)
#发送邮件服务器1
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

my_sender = 'hacker9090@126.com' # 发件人邮箱账号hacker9090@126.com
my_pass = ''  # 发件人邮箱密码
my_user = '2698392815@qq.com' # 收件人邮箱账号，我这边发送给自己'2698392815@qq.com'

def mail(i):
    try:
        msg = MIMEText(i, 'plain', 'utf-8')
        sender_name = 'M9KJ-TEAM'
        msg['From'] = formataddr([sender_name, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        my_name = 'M9KJ-TEAM'
        msg['To'] = formataddr([my_name, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "[外网资产]端口监控-端口存在异常！" # 邮件的主题，也可以说是标题
        server = smtplib.SMTP_SSL("smtp.126.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        time.sleep(5)
        print ('等待5秒关闭链接。。。')
        server.quit()  # 关闭连接
        ret = True
    except Exception as e:
        print(e)
        ret = False
    return ret
