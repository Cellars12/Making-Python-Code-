import random
import json
import os

def intro():
    print("환영합니다! 당신은 자원을 채굴하는 광부입니다.")
    print("광산에 들어가 자원을 채굴하고, 자원을 판매하여 장비를 업그레이드하세요.")
    print("자원 종류: 철, 금, 다이아몬드")
    print("현재 자원: 철 0, 금 0, 다이아몬드 0, 금액: 0, 레벨: 1, 경험치: 0, 체력: 100")

def mine_resources(level):
    resources = {
        '철': random.randint(0, 5 + level),
        '금': random.randint(0, 3 + level),
        '다이아몬드': random.randint(0, 1 + level)
    }
    return resources

def sell_resources(resources):
    price_per_unit = {
        '철': 2,
        '금': 10,
        '다이아몬드': 50
    }
    earnings = sum(resources[res] * price_per_unit[res] for res in resources)
    return earnings

def random_event():
    event = random.choice(["폭발", "자원 발견", "광부의 부상", "아무 일 없음"])
    if event == "폭발":
        print("폭발! 체력을 10 잃었습니다.")
        return -10  # 체력 감소
    elif event == "광부의 부상":
        print("광부가 부상당했습니다. 체력을 5 잃었습니다.")
        return -5
    return 0

def shop(total_money, resources):
    print("상점에 오신 것을 환영합니다!")
    print("아이템 구매: ")
    print("1. 철 5개 - 8 금")
    print("2. 금 3개 - 25 금")
    print("3. 다이아몬드 1개 - 40 금")
    print("4. 장비 (채굴 효율 +2) - 50 금")
    print("5. 체력 회복 물약 - 15 금")
    print("6. 나가기")

    choice = input("구매할 아이템 번호를 입력하세요: ")
    if choice == "1" and total_money >= 8:
        total_money -= 8
        resources['철'] += 5
        print("철 5개를 구매했습니다!")
    elif choice == "2" and total_money >= 25:
        total_money -= 25
        resources['금'] += 3
        print("금 3개를 구매했습니다!")
    elif choice == "3" and total_money >= 40:
        total_money -= 40
        resources['다이아몬드'] += 1
        print("다이아몬드 1개를 구매했습니다!")
    elif choice == "4" and total_money >= 50:
        total_money -= 50
        print("장비를 구매했습니다! 채굴 효율이 증가했습니다.")
    elif choice == "5" and total_money >= 15:
        total_money -= 15
        print("체력 회복 물약을 구매했습니다! 체력이 20 회복됩니다.")
        return total_money, resources, 20  # 체력 회복
    elif choice == "6":
        return total_money, resources, 0
    else:
        print("금액이 부족하거나 잘못된 선택입니다.")
    
    return total_money, resources, 0

def complete_quest(experience):
    print("퀘스트를 완료했습니다! 경험치를 15 얻습니다.")
    experience += 15
    return experience

def save_game(state):
    with open("save_game.json", "w") as f:
        json.dump(state, f)

def load_game():
    if os.path.exists("save_game.json"):
        with open("save_game.json", "r") as f:
            return json.load(f)
    return None

def play_game():
    resources = {'철': 0, '금': 0, '다이아몬드': 0}
    total_money = 0
    level = 1
    experience = 0
    health = 100
    intro()
    
    while True:
        print(f"현재 체력: {health}, 경험치: {experience}")
        action = input("행동을 선택하세요 (1: 채굴, 2: 판매, 3: 상점, 4: 퀘스트 완료, 5: 저장, 6: 불러오기, 7: 종료): ")
        
        if action == "1":
            mined = mine_resources(level)
            resources['철'] += mined['철']
            resources['금'] += mined['금']
            resources['다이아몬드'] += mined['다이아몬드']
            print(f"채굴한 자원: 철 {mined['철']}, 금 {mined['금']}, 다이아몬드 {mined['다이아몬드']}")
            health += random_event()  # 사고로 인한 체력 감소

        elif action == "2":
            earnings = sell_resources(resources)
            total_money += earnings
            print(f"판매한 자원: 철 {resources['철']}, 금 {resources['금']}, 다이아몬드 {resources['다이아몬드']}, 수익: {earnings}, 총 금액: {total_money}")
            resources = {'철': 0, '금': 0, '다이아몬드': 0}  # 판매 후 자원 초기화

        elif action == "3":
            total_money, resources, health_recover = shop(total_money, resources)
            health += health_recover

        elif action == "4":
            experience = complete_quest(experience)

        elif action == "5":
            save_game({
                'resources': resources,
                'total_money': total_money,
                'level': level,
                'experience': experience,
                'health': health
            })
            print("게임이 저장되었습니다.")

        elif action == "6":
            loaded_state = load_game()
            if loaded_state:
                resources = loaded_state['resources']
                total_money = loaded_state['total_money']
                level = loaded_state['level']
                experience = loaded_state['experience']
                health = loaded_state['health']
                print("게임이 불러와졌습니다.")
            else:
                print("저장된 게임이 없습니다.")

        elif action == "7":
            print("게임 종료. 최종 자원:", resources, "최종 금액:", total_money)
            break
        
        else:
            print("올바른 선택이 아닙니다. 다시 시도하세요.")

        # 레벨업 체크
        if experience >= 20:
            level += 1
            experience = 0
            print(f"레벨업! 현재 레벨: {level}")

        if health <= 0:
            print("체력이 다 떨어졌습니다. 게임 오버!")
            break

if __name__ == "__main__":
    play_game()
