import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')  # 这里是你的信件中的内容
msg['From'] = '1307336401@qq.com'  # 这里是发送人的邮箱.
msg['To'] = '1307336401@qq.com'  # 这里是接收信件人的邮箱
msg['Subject'] = 'an email'  # 这里是信件的标题

server = smtplib.SMTP('smtp.qq.com') # POP3服务器地址为“pop.qq.com”，SMTP服务器地址为“smtp.qq.com”
server.login(user='1307336401@qq.com', password='butmjmvokhjsbabf')   #将password替换成授权码
# user 是发送人的邮箱, password 是你的授权码!授权码!授权码!(这不是我生日.)
server.send_message(msg=msg)

server.close()
