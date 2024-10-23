import random

def get_user_choice():
    user_input = input("가위, 바위, 보 중에서 선택하세요: ")
    while user_input not in ['가위', '바위', '보']:
        print("잘못된 선택입니다. 다시 선택하세요.")
        user_input = input("가위, 바위, 보 중에서 선택하세요: ")
    return user_input

def get_computer_choice():
    choices = ['가위', '바위', '보']
    return random.choice(choices)

def determine_winner(user, computer):
    if user == computer:
        return "무승부!"
    elif (user == '가위' and computer == '보') or \
         (user == '바위' and computer == '가위') or \
         (user == '보' and computer == '바위'):
        return "당신이 이겼습니다!"
    else:
        return "컴퓨터가 이겼습니다!"

def play_game():
    print("가위 바위 보 게임에 오신 것을 환영합니다!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"당신의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
