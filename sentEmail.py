# -*- coding: UTF-8 -*-
import datetime
'''
发送txt文本邮件
'''
#========================================== 
# 导入smtplib和MIMEText 
#========================================== 
from email.mime.text import MIMEText 
import smtplib 
#========================================== 
# 要发给谁，这里发给2个人 
#========================================== 
mailto_list=["38643987@qq.com","787687312@qq.com"] 
#========================================== 
# 设置服务器，用户名、口令以及邮箱的后缀 
#========================================== 
##mail_host="mail.petrochina.com.cn"  #设置服务器
##mail_user="xuleo"
##mail_pass="820729"
##mail_postfix="petrochina.com.cn"

mail_host="smtp.qq.com"  #设置服务器
mail_user="38643987"
mail_pass="xulei820729"
mail_postfix="qq.com"
#========================================== 
# 发送邮件 
#========================================== 
def send_mail(to_list,sub,content): 
  ''''' 
  to_list:发给谁 
  sub:主题 
  content:内容 
  send_mail("aaa@126.com","sub","content") 
  '''
  me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
  msg = MIMEText(content) 
  msg['Subject'] = sub 
  msg['From'] = me 
  msg['To'] = ";".join(to_list) 
  try: 
    s = smtplib.SMTP() 
    s.connect(mail_host) 
    s.login(mail_user,mail_pass) 
    s.sendmail(me, to_list, msg.as_string()) 
    s.close() 
    return True
  except Exception, e: 
    print str(e) 
    return False
if __name__ == '__main__':
  nowStr=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  news="hello,world"
  if send_mail(mailto_list,nowStr,news): 
    print "mail success"
  else: 
    print "mail fail"
