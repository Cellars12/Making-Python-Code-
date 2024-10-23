import calendar

# 연도와 월을 입력받습니다.
year = int(input("연도를 입력하세요 (예: 2023): "))
month = int(input("월을 입력하세요 (1-12): "))

# 달력을 출력합니다.
print(calendar.month(year, month))
