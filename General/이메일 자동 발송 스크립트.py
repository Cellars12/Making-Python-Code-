import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    from_email = '이메일 주소를 작성해주세요.'
    password = '이메일 비밀번호를 작성해주세요.'
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

subject = '이메일 제목을 작성해주세요.'
body = '이메일 내용을 작성해주세요.'
to_email = '이메일 주소를 작성해주세요.'
send_email(subject, body)
