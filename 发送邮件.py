import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = "linux_redhat@sina.com"
from_passwd = "xxxxxxxx"
to_addr = ['489543181@qq.com']

smtp_obj = smtplib.SMTP_SSL("smtp.sina.com", 465)
# smtp_obj = smtplib.SMTP("smtp.sina.com", 25)
smtp_obj.login(from_addr, from_passwd)
smtp_obj.set_debuglevel(1)

msg = MIMEMultipart()
msg['From'] = _format_addr('Python <%s>' % from_addr)  # "utf-8" 新浪邮箱加"utf-8"报错
msg['To'] = Header("傻瓜", "utf-8")
msg['Subject'] = Header('some test', 'utf-8')

msg_body = '''
<h5>This is the newest python sourcecode, please check!<h5>
<p>
    <img src="cid:image1">
</p>
'''
msg.attach(MIMEText(msg_body, "html", "utf-8"))  # "plain"

with open('main.py', 'rb') as f:
    att1 = MIMEText(f.read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment;filename="main.py"'
    msg.attach(att1)

with open('医药筛选系统.py', 'rb') as f:
    att2 = MIMEText(f.read(), 'base64', 'utf-8')
    att2['Content-Type'] = 'application/octet-stream'
    att2['Content-Disposition'] = 'attachment;filename="医药筛选系统.py"'
    msg.attach(att2)

with open('data/20190308115530905.png', 'rb') as f:
    image = MIMEImage(f.read())
    image.add_header('Content-ID', '<image1>')
    msg.attach(image)

try:
    smtp_obj.sendmail(from_addr, to_addr, msg.as_string())
    print('发送邮件成功！')
except smtplib.SMTPException as e:
    print('Error: 无法发送邮件')
    print(e)
