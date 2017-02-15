#!/usr/bin/python
# -*- coding: UTF-8 -*-



import smtplib
from email.mime.text import MIMEText


def send_msg(Subject,msg):
    _user = "772575249@qq.com"
    _pwd  = "xbjdncgiajdgbbeh"
    _to   = "15008487521@163.com"

    msg = MIMEText(msg)
    msg["Subject"] = Subject
    msg["From"]    = _user
    msg["To"]      = _to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied,%s"%e)

if __name__=="__main__":
    send_msg("这是一封测试邮件的主题","这是一封测试邮件的内容")

# # 第三方 SMTP 服务
# mail_host="smtp.qq.com"  #设置服务器
# mail_user="772575249@qq.com"    #用户名
# mail_pass="xbjdncgiajdgbbeh"   #口令
#
#
# sender = '772575249@qq.com'
# receivers = ['15008487521@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] =  Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
#     smtpObj.login(mail_user,mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print ("邮件发送成功")
# except smtplib.SMTPException as e:
#
#     print (e)