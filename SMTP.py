# 用于发送邮件的模块
import smtplib

# QQ邮件
# 1> 配置邮箱SMTP服务器的主机地址，将来使用这个服务器收发邮件。
HOST = 'smtp.qq.com'
# # 2> 配置服务的端口，默认的邮件端口是25.
PORT = '465'
# # 3> 指定发件人和收件人。
FROM = '842075291@qq.com'
TO = '842075291@qq.com'
# # 4> 邮件标题
SUBJECT = '这是一封测试邮件'
# # 5> 邮件内容
CONTENT = '这是<987456123@qq.com>发送过来的邮件。请注意查收！'

# # 创建邮件发送对象
# # 普通的邮件发送形式
#smtp_obj = smtplib.SMTP()

# # 数据在传输过程中会被加密。
smtp_obj = smtplib.SMTP_SSL('smtp.qq.com','465')

# # 需要进行发件人的认证，授权。
# # smtp_obj就是一个第三方客户端对象
smtp_obj.connect(host=HOST, port=PORT)

# # 如果使用第三方客户端登录，要求使用授权码，不能使用真实密码，防止密码泄露。
res = smtp_obj.login(user=FROM, password='iyixfaudyboybegd')
print('登录结果：', res)
# # 发送邮件
msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'Subject: {}'.format(SUBJECT), '', CONTENT])
smtp_obj.sendmail(from_addr=FROM, to_addrs=[TO], msg=msg.encode('utf-8'))