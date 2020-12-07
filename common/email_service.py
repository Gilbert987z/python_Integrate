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
def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# indent用于缩进显示:
def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串:
                    value = decode_str(value)
                    subject = value
                    # print(subject)
                else:
                    # 需要解码Email地址:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            # todo 注释掉
            # print('%s%s: %s' % ('  ' * indent, header, value))
    # todo 注释掉
    # if (msg.is_multipart()):
    #     # 如果邮件对象是一个MIMEMultipart,
    #     # get_payload()返回list，包含所有的子对象:
    #     parts = msg.get_payload()
    #     for n, part in enumerate(parts):
    #         print('%spart %s' % ('  ' * indent, n))
    #         print('%s--------------------' % ('  ' * indent))
    #         # 递归打印每一个子对象:
    #         print_info(part, indent + 1)
    # else:
    #     # 邮件对象不是一个MIMEMultipart,
    #     # 就根据content_type判断:
    #     content_type = msg.get_content_type()
    #     if content_type == 'text/plain' or content_type == 'text/html':
    #         # 纯文本或HTML内容:
    #         content = msg.get_payload(decode=True)
    #         # 要检测文本编码:
    #         charset = guess_charset(msg)
    #         if charset:
    #             content = content.decode(charset)
    #         # print(type(content))
    #         print('%sText: %s' % ('  ' * indent, content + '...'))
    #     else:
    #         # 不是文本,作为附件处理:
    #         print('%sAttachment: %s' % ('  ' * indent, content_type))
    return subject  #返回subject


def get_email_subject():
    # 输入邮件地址, 口令和POP3服务器地址:
    email = 'zhangzhe@yodosmart.com'
    password = 'Yodo1234'
    pop3_server = 'pop3.yodosmart.com'

    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    #todo 注释掉
    # server.set_debuglevel(1)

    # 可选:打印POP3服务器的欢迎文字:
    #todo 注释掉
    # print(server.getwelcome().decode('utf-8'))

    # 身份认证:
    server.user(email)
    server.pass_(password)
    # stat()返回邮件数量和占用空间:
    #todo 注释掉
    # print('Messages: %s. Size: %s' % server.stat()

    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    #todo 注释掉
    # print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    subject = print_info(msg)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()

    return subject




if __name__ == '__main__':
    #获取subject
    print(get_email_subject())