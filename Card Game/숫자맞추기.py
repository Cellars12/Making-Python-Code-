import random

def play_guessing_game():
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 100 사이의 숫자를 맞추세요.")
    
    # 컴퓨터가 1부터 100 사이의 랜덤 숫자를 선택합니다.
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("당신의 추측: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력하세요.")
                continue

            if guess < secret_number:
                print("더 큰 숫자를 시도해 보세요.")
            elif guess > secret_number:
                print("더 작은 숫자를 시도해 보세요.")
            else:
                print(f"축하합니다! {attempts}번 만에 맞추셨습니다.")
                break  # 숫자를 맞추면 반복 종료

        except ValueError:
            print("유효한 숫자를 입력하세요.")

    restart = input("다시 하시겠습니까? (y/n): ").lower()
    if restart == 'y':
        play_guessing_game()
    else:
        print("게임을 종료합니다.")

# 게임 실행
if __name__ == "__main__":
    play_guessing_game()
