#!/usr/bin/python
# -*- coding: UTF-8 -*-



import smtplib
from email.mime.text import MIMEText


def send_msg(Subject,msg):
    _user = "youEmail"
    _pwd  = "passwd"
    _to   = "to_email"

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


