import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

class Smtp:

    def __init__(self):
        # 发件人
        self.from_name = "赵博"
        # 发件邮箱
        self.from_addr = "974475528@qq.com"
        # 发件邮箱授权码
        self.from_pwd = "hgfxucsiaeurbfaa"
        # SMTP服务器地址，QQ邮箱的SMTP地址是"smtp.qq.com"
        self.smtp_srv = "smtp.qq.com"
        # SMTP服务器端口
        self.smtp_port = 465



    def loginsmtp(self):
        self.srv = smtplib.SMTP_SSL(self.smtp_srv.encode(),self.smtp_port)
        print("连接成功！！")
        # 使用授权码登录邮箱
        self.srv.login(self.from_addr, self.from_pwd)
        print("登录成功！！")

    def logout(self):
        # 退出登录
        self.srv.quit()

    # 发送文本信息
    def sendmsg(self,msg,title,to_addr):
        message = MIMEText(msg,'plain','utf-8')  # 发送的内容
        message['From'] = formataddr([self.from_name, self.from_addr])
        message['Subject'] = title  # 邮件主题
        try:
            self.srv.sendmail(self.from_addr,to_addr,message.as_string())
        except Exception as e:
            print('邮件发送失败--' + str(e))
        print('邮件发送成功')

    # 发送带附件的信息
    def sendwithfile(self,msg,title,filepath,filename,to_addr):
        message = MIMEMultipart('related')
        message['From'] = formataddr([self.from_name, self.from_addr])
        message['Subject'] = title  # 邮件主题

        # 邮件正文内容
        msg_text = MIMEText(msg,'plain','utf-8')

        # 构造附件
        addfile = MIMEText(open(filepath,'rb').read(),'base64','utf-8')
        # 指定文件格式类型
        addfile["Content-Type"] = "application/octet-stream"
        # 文件名
        addfile["Content-Disposition"] = "attachment; filename=" + filename

        # MIMEMultipart对象附加text,img,attach内容
        message.attach(msg_text)
        message.attach(addfile)

        try:
            self.srv.sendmail(self.from_addr,to_addr,message.as_string())
        except Exception as e:
            print('邮件发送失败--' + str(e))
        print('邮件发送成功')





