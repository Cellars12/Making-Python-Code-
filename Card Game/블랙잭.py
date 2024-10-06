import random

# 카드 덱 생성
def create_deck():
    suits = ['하트', '다이아몬드', '클럽', '스페이드']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '잭', '퀸', '킹', '에이스']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# 카드의 점수 계산
def card_value(card):
    rank, _ = card
    if rank in ['잭', '퀸', '킹']:
        return 10
    elif rank == '에이스':
        return 11  # 에이스는 11로 시작하지만, 상황에 따라 1로 조정 가능
    else:
        return int(rank)

# 손의 점수 계산
def calculate_hand_value(hand):
    value = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == '에이스')
    
    # 에이스를 11에서 1로 조정
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

# 게임 진행
def play_blackjack():
    while True:
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        print(f"딜러의 카드: {dealer_hand[0]}")
        print(f"플레이어의 카드: {player_hand}, 총 점수: {calculate_hand_value(player_hand)}")

        while True:
            action = input("카드를 더 받으시겠습니까? ('히트' 또는 '스탠드' 입력, '종료'로 종료): ").lower()
            if action == '히트':
                player_hand.append(deck.pop())
                player_value = calculate_hand_value(player_hand)
                print(f"플레이어의 카드: {player_hand}, 총 점수: {player_value}")
                if player_value > 21:
                    print("버스트! 딜러가 이겼습니다.")
                    break
            elif action == '스탠드':
                break
            elif action == '종료':
                restart = input("게임을 종료하고 재시작 하시겠습니까? (네/아니요): ").lower()
                if restart == '네':
                    print("새 게임을 시작합니다.")
                    break  # 새로운 게임 시작
                else:
                    print("게임을 종료합니다.")
                    return  # 종료
            else:
                print("잘못된 입력입니다! '히트', '스텐드' 또는 '아니요'를 입력하세요.")

        if player_value <= 21:  # 플레이어가 버스트가 아닐 때만 딜러의 차례
            dealer_value = calculate_hand_value(dealer_hand)
            print(f"딜러의 카드: {dealer_hand}, 총 점수: {dealer_value}")

            while dealer_value < 17:
                dealer_hand.append(deck.pop())
                dealer_value = calculate_hand_value(dealer_hand)
                print(f"딜러의 카드: {dealer_hand}, 총 점수: {dealer_value}")

            if dealer_value > 21 or player_value > dealer_value:
                print("당신이 이겼습니다!")
            elif player_value < dealer_value:
                print("딜러가 이겼습니다!")
            else:
                print("무승부입니다!")

# 게임 실행
if __name__ == "__main__":
    play_blackjack()
