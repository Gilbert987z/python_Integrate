#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def send_email_carry_txt(receviers, msg_tile, msg_content, msg_attach):
    '''

    :param receviers:
    :param msg_tile:
    :param msg_content:
    :param msg_attach:
    :return:
    '''
    sender = 'zhangzhe@yodosmart.com'
    #todo 可以发给很多人 到时候要改
    receivers = [receviers]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = 'zhangzhe@yodosmart.com'
    message['To'] = receviers
    subject = msg_tile    # 这里是信件的标题
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(msg_content, 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(msg_attach, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # 分割
    (filepath, filename) = os.path.split(msg_attach)
    print(filename)
    # 附件名称为非中文时的写法
    # att1["Content-Disposition"] = 'attachment; filename =' +filename
    # 附件名称为中文时的写法
    att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", filename))

    message.attach(att1)

    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)

    try:
        smtpObj = smtplib.SMTP('smtp.yodosmart.com')
        smtpObj.login(user='zhangzhe@yodosmart.com', password='Yodo1234')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


#todo 获取邮箱
def get_email_content():
    '''

    :return:
    '''
    useraccount = '1307336401@qq.com'
    password = 'butmjmvokhjsbabf'

    # 邮件服务器地址,以下为网易邮箱
    pop3_server = 'pop.qq.com'

    # 开始连接到服务器
    server = poplib.POP3(pop3_server)

    # 打开或者关闭调试信息，为打开，会在控制台打印客户端与服务器的交互信息
    server.set_debuglevel(1)

    # 打印POP3服务器的欢迎文字，验证是否正确连接到了邮件服务器
    print(server.getwelcome().decode('utf8'))

    # 开始进行身份验证
    server.user(useraccount)
    server.pass_(password)

    # 返回邮件总数目和占用服务器的空间大小（字节数）， 通过stat()方法即可
    email_num, email_size = server.stat()
    print("消息的数量: {0}, 消息的总大小: {1}".format(email_num, email_size))

    # 使用list()返回所有邮件的编号，默认为字节类型的串
    rsp, msg_list, rsp_siz = server.list()
    print("服务器的响应: {0},\n消息列表： {1},\n返回消息的大小： {2}".format(rsp, msg_list, rsp_siz))

    print('邮件总数： {}'.format(len(msg_list)))

    # 下面单纯获取最新的一封邮件
    total_mail_numbers = len(msg_list)
    rsp, msglines, msgsiz = server.retr(total_mail_numbers)
    # print("服务器的响应: {0},\n原始邮件内容： {1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))

    msg_content = b'\r\n'.join(msglines).decode('gbk')

    msg = Parser().parsestr(text=msg_content)
    print('解码后的邮件信息:\n{}'.format(msg))

    # 关闭与服务器的连接，释放资源
    server.close()

    return msg


get_email_content()

# if __name__ == '__main__':
#     send_email_carry_txt(receviers='1307336401@qq.com', msg_tile='maintest', msg_content='msg_test', msg_attach='FOTA.xlsx')