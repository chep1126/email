import requests
import re
import time
from send_email import send_msg

def query():
    url = "https://yz.chsi.com.cn/apply/cjcx/getSch.jsp?ssdm=51&ts=1487169927492"

    req = requests.get(url=url)
    rex = re.compile(r'(?<=\[CDATA\[)[\u4e00-\u9fa5]+(?=\]\])')
    subject = "现在可以查询成绩的学校"
    result = rex.findall(req.text)
    msg_str = ""
    for r in result:
        msg_str = msg_str + r + "\n"
    send_msg(subject, msg_str)

if __name__=="__main__":
    while(True):
        time.sleep(600)
        query()
