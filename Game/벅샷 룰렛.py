import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 3  # 초기 생명 수
        self.items = []  # 아이템 목록

    def take_turn(self):
        print(f"\n{self.name}의 차례입니다!")
        input("총을 쏘려면 Enter 키를 누르세요...")

    def use_item(self):
        if self.items:
            print(f"{self.name}의 아이템: {', '.join(self.items)}")
            choice = input("사용할 아이템을 선택하세요 (없으면 그냥 Enter): ")
            if choice in self.items:
                self.items.remove(choice)
                print(f"{self.name}이(가) {choice}를 사용했습니다!")
                return choice  # 사용한 아이템 반환
        else:
            print(f"{self.name}은(는) 아이템이 없습니다.")
        return None

def setup_chamber():
    chamber = [0] * 5 + [1]  # 5개의 안전 슬롯과 1개의 장전된 슬롯
    random.shuffle(chamber)  # 슬롯 섞기
    return chamber

def buckshot_roulette():
    print("벅샷 룰렛에 오신 것을 환영합니다!")

    player_count = int(input("몇 명이 플레이할까요? (2명 이상 입력): "))
    while player_count < 2:
        print("플레이어 수는 2명 이상이어야 합니다.")
        player_count = int(input("몇 명이 플레이할까요? (2명 이상 입력): "))

    players = [Player(input(f"플레이어 {i + 1} 이름을 입력하세요: ")) for i in range(player_count)]

    # 아이템 초기화 (무작위로 아이템 추가)
    item_list = ['구급상자', '방탄복', '특수탄']
    for player in players:
        player.items.append(random.choice(item_list))  # 각 플레이어에게 아이템 하나 부여

    while len(players) > 1:
        chamber = setup_chamber()  # 매 턴마다 새 슬롯 생성

        for player in players:
            if player.health <= 0:
                print(f"{player.name}은(는) 사망했습니다!")
                continue

            # 아이템 사용
            item_used = player.use_item()
            if item_used == '구급상자':
                player.health += 1
                print(f"{player.name}의 생명이 1 증가했습니다! (현재 생명: {player.health})")
                continue
            elif item_used == '방탄복':
                print(f"{player.name}이(가) 방탄복을 사용하여 이번 턴에 피격을 면했습니다!")
                chamber.pop(0)  # 슬롯 제거 없이 턴 종료
                continue
            
            player.take_turn()

            hit = chamber.pop(0)  # 슬롯 확인 후 제거
            if hit == 1:
                player.health -= 1
                print(f"피격! {player.name}의 남은 생명: {player.health}")
            else:
                print(f"{player.name}은(는) 허공에 쏘았습니다! 다음 차례로 넘어갑니다.")

            if player.health <= 0:
                print(f"{player.name}은(는) 사망했습니다!")

        print("\n현재 상태:")
        for player in players:
            print(f"{player.name}: 생명 = {player.health}, 아이템 = {', '.join(player.items)}")

        # 사망한 플레이어 제거
        players = [player for player in players if player.health > 0]

    if players:
        print(f"{players[0].name}이(가) 승리했습니다!")
    else:
        print("모든 플레이어가 사망했습니다! 게임 종료.")

if __name__ == "__main__":
    buckshot_roulette()
