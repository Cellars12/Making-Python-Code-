import schedule
import time
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
import requests

# 이메일 알림 함수
def send_email(task):
    from_email = "your_email@gmail.com"  # 자신의 이메일 주소
    password = "your_password"             # 이메일 비밀번호
    to_email = "recipient_email@example.com"  # 수신자 이메일 주소

    subject = "할 일 알림"
    body = f"알림: {task}입니다!"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())

# SMS 알림 함수
def send_sms(task):
    account_sid = 'your_account_sid'          # Twilio Account SID
    auth_token = 'your_auth_token'            # Twilio Auth Token
    from_phone = 'your_twilio_phone'          # Twilio에서 받은 전화번호
    to_phone = 'recipient_phone'               # 수신자 전화번호

    client = Client(account_sid, auth_token)
    client.messages.create(body=f"알림: {task}입니다!", from_=from_phone, to=to_phone)

# 디스코드 알림 함수
def send_discord_message(task):
    webhook_url = "your_discord_webhook_url"  # 디스코드 웹훅 URL
    message = {"content": f"알림: {task}입니다!"}
    requests.post(webhook_url, json=message)

# 작업 함수
def job(task):
    print(f"알림: {task}입니다!")  # 콘솔에 알림 출력
    send_email(task)             # 이메일로 알림 보내기
    send_sms(task)               # SMS로 알림 보내기
    send_discord_message(task)   # 디스코드로 알림 보내기

# 일정 추가 함수
def add_task():
    task = input("할 일을 입력하세요: ")
    time_str = input("알림 시간을 입력하세요 (예: 14:30): ")
    hour, minute = map(int, time_str.split(':'))
    
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(job, task)

# 스케줄러 실행 함수
def run_scheduler():
    print("스케줄러가 시작되었습니다. (종료하려면 Ctrl+C를 누르세요)")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n스케줄러가 종료되었습니다.")

if __name__ == "__main__":
    while True:
        add_task()
        another = input("또 다른 일정을 추가하시겠습니까? (y/n): ")
        if another.lower() != 'y':
            break

    run_scheduler()
