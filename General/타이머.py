import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('시간이 되었습니다.')


t = input('초를 입력해주세요: ')

countdown(int(t))
