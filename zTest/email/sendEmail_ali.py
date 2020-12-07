import smtplib
from email.mime.text import MIMEText

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
msg['From'] = 'zhangzhe@yodosmart.com'  # 这里是发送人的邮箱.
msg['To'] = '1307336401@qq.com'  # 这里是接收信件人的邮箱
msg['Subject'] = 'an email'  # 这里是信件的标题

server = smtplib.SMTP('smtp.yodosmart.com') # POP3服务器地址为“pop.qq.com”，SMTP服务器地址为“smtp.qq.com”
server.login(user='zhangzhe@yodosmart.com', password='Yodo1234')   #将password替换成授权码
# user 是发送人的邮箱, password 是你的授权码!授权码!授权码!(这不是我生日.)
server.send_message(msg=msg)

server.close()
