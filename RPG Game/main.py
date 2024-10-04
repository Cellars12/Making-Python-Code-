import random
import json

class Character:
    def __init__(self, name, health, attack, level=1, character_class="전사"):
        self.name = name
        self.health = health
        self.attack = attack
        self.level = level
        self.experience = 0
        self.inventory = []
        self.skills = []
        self.gold = 0
        self.character_class = character_class

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}가 {damage}의 피해를 입었습니다! 남은 체력: {self.health}")

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name}가 {enemy.name}를 공격합니다! {damage}의 피해를 입혔습니다.")
        enemy.take_damage(damage)

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name}가 {amount} 경험치를 얻었습니다! 총 경험치: {self.experience}")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack += 5
        self.experience = 0
        print(f"{self.name}가 레벨 {self.level}로 상승했습니다! 체력: {self.health}, 공격력: {self.attack}")
        self.learn_new_skills()

    def learn_new_skills(self):
        warrior_skills = {
            100: "강타",
            200: "맹공격",
            300: "지진",
            400: "전투의 외침",
            500: "방어 자세",
            600: "분노의 일격",
            700: "철벽 방어",
            800: "전투 장벽",
            900: "광폭화"
        }
        mage_skills = {
            100: "불꽃구슬",
            200: "냉기 마법",
            300: "전기 충격",
            400: "치유 마법",
            500: "시간 정지",
            600: "대지의 힘",
            700: "영혼의 폭풍",
            800: "천상의 기원",
            900: "우주 마법"
        }

        if self.character_class == "전사" and self.level in warrior_skills:
            skill = warrior_skills[self.level]
            self.learn_skill(skill)
        elif self.character_class == "마법사" and self.level in mage_skills:
            skill = mage_skills[self.level]
            self.learn_skill(skill)

    def learn_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"{self.name}가 스킬 '{skill}'을(를) 배웠습니다!")

    def use_item(self, item):
        if item in self.inventory:
            if item == "치료제":
                self.health += 30
                self.inventory.remove(item)
                print(f"{self.name}가 {item}를 사용하여 체력을 30 회복했습니다! 남은 체력: {self.health}")
            elif item == "경험치 병":
                xp_gain = random.randint(20, 50)
                self.gain_experience(xp_gain)
                self.inventory.remove(item)
                print(f"{self.name}가 {item}를 사용하여 경험치를 {xp_gain} 얻었습니다!")
            else:
                print(f"{item}는 사용할 수 없는 아이템입니다.")
        else:
            print(f"{item}이(가) 인벤토리에 없습니다.")

    def use_skill(self, skill, enemy):
        if skill in self.skills:
            damage = random.randint(15, self.attack + 10)
            print(f"{self.name}가 스킬 '{skill}'로 {enemy.name}를 공격합니다! {damage}의 피해를 입혔습니다.")
            enemy.take_damage(damage)
        else:
            print(f"{self.name}는 스킬 '{skill}'을(를) 사용할 수 없습니다.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name}가 {amount}골드를 얻었습니다! 총 골드: {self.gold}")

class Shop:
    def __init__(self):
        self.items = {
            "치료제": 20,
            "강화 포션": 50,
            "경험치 병": 30,
        }

    def show_items(self):
        print("상점 아이템:")
        for item, price in self.items.items():
            print(f"{item} - {price}골드")

    def buy_item(self, player, item):
        if item in self.items:
            price = self.items[item]
            if player.gold >= price:
                player.gold -= price
                player.inventory.append(item)
                print(f"{player.name}가 {item}를 구매했습니다!")
            else:
                print("골드가 부족합니다.")
        else:
            print("존재하지 않는 아이템입니다.")

class Game:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.current_quest = None
        self.shop = Shop()
        self.quests = [
            "고블린 3마리 처치하기",
            "슬라임 5마리 처치하기",
            "늑대 2마리 처치하기",
            "마을 주민을 도와주기",
            "전설의 아이템 찾기",
            "신비한 물약을 모으기",
            "보물 찾기",
            "마법사의 탑 정복하기",
            "어둠의 세력 처치하기",
            "전투 훈련소에서 훈련하기",
            "사라진 마을 탐색하기",
            "미궁을 탐험하기",
            "적의 기지를 공격하기",
            "상인을 도와주기",
            "고대 유적 조사하기",
            "마법의 수정 찾기",
            "불의 신전 정화하기",
            "해적의 보물 찾기",
            "왕국을 구하기",
            "전쟁의 영웅 찾기",
            "여행하는 상인 보호하기",
            "용의 알 찾기",
            "악당의 소굴 정리하기",
            "가장 강력한 전사 찾기",
            "신비한 성물 수집하기",
            "사냥꾼의 훈련 받기",
            "도둑을 쫓아내기",
            "마법서를 찾아오기",
            "정글의 괴물 처치하기",
            "성 안의 비밀 조사하기",
            "운명의 수레바퀴 회전시키기",
            "마법의 열쇠 찾기"
        ]

    def choose_character(self):
        print("캐릭터를 선택하세요:")
        print("1. 전사 (체력: 100, 공격력: 20)")
        print("2. 마법사 (체력: 80, 공격력: 30)")
        
        choice = input("캐릭터 번호를 입력하세요: ")
        if choice == '1':
            self.player = Character("전사", 100, 20, character_class="전사")
            self.player.learn_skill("강타")
        elif choice == '2':
            self.player = Character("마법사", 80, 30, character_class="마법사")
            self.player.learn_skill("불꽃구슬")
        else:
            print("잘못된 선택입니다. 전사로 설정합니다.")
            self.player = Character("전사", 100, 20, character_class="전사")

    def create_enemies(self, count):
        enemy_types = [
            ("고블린", random.randint(50, 80), random.randint(5, 10)),
            ("슬라임", random.randint(30, 60), random.randint(3, 8)),
            ("늑대", random.randint(40, 70), random.randint(8, 12)),
        ]
        for i in range(count):
            enemy_type = random.choice(enemy_types)
            enemy = Character(enemy_type[0], enemy_type[1], enemy_type[2])
            self.enemies.append(enemy)
            print(f"{enemy.name}가 나타났습니다! 체력: {enemy.health}, 공격력: {enemy.attack}")

    def battle(self):
        while self.player.is_alive() and self.enemies:
            action = input("행동을 선택하세요 (1: 공격, 2: 아이템 사용, 3: 스킬 사용, 4: 상점): ")
            if action == '1':
                for enemy in list(self.enemies):
                    self.player.attack_enemy(enemy)
                    if not enemy.is_alive():
                        print(f"{enemy.name}가 쓰러졌습니다!")
                        self.player.gain_experience(50)
                        self.player.add_gold(random.randint(5, 20))
                        self.enemies.remove(enemy)
                    else:
                        enemy.attack_enemy(self.player)
                    if not self.player.is_alive():
                        print("게임 오버! 당신은 패배했습니다.")
                        return
            elif action == '2':
                self.use_item()
            elif action == '3':
                self.use_skill()
            elif action == '4':
                self.shop_menu()
            else:
                print("잘못된 선택입니다.")

            print("")

        if self.player.is_alive():
            print("축하합니다! 모든 적을 처치했습니다!")
            self.complete_quest()

    def use_item(self):
        if self.player.inventory:
            print("사용할 아이템을 선택하세요:")
            for idx, item in enumerate(self.player.inventory, start=1):
                print(f"{idx}. {item}")
            choice = int(input("아이템 번호를 입력하세요: ")) - 1
            if 0 <= choice < len(self.player.inventory):
                item_to_use = self.player.inventory[choice]
                self.player.use_item(item_to_use)
            else:
                print("잘못된 선택입니다.")
        else:
            print("인벤토리에 아이템이 없습니다.")

    def use_skill(self):
        if self.player.skills:
            print("사용할 스킬을 선택하세요:")
            for idx, skill in enumerate(self.player.skills, start=1):
                print(f"{idx}. {skill}")
            choice = int(input("스킬 번호를 입력하세요: ")) - 1
            if 0 <= choice < len(self.player.skills):
                target_enemy = random.choice(self.enemies)
                self.player.use_skill(self.player.skills[choice], target_enemy)
            else:
                print("잘못된 선택입니다.")
        else:
            print("스킬이 없습니다.")

    def shop_menu(self):
        while True:
            self.shop.show_items()
            action = input("아이템 구매를 원하시면 아이템 이름을 입력하세요. 상점을 나가려면 '종료'를 입력하세요: ")
            if action == '종료':
                break
            else:
                self.shop.buy_item(self.player, action)

    def complete_quest(self):
        if self.current_quest:
            print(f"퀘스트 '{self.current_quest}' 완료! 보상을 받았습니다.")
            self.player.add_gold(50)
            self.current_quest = random.choice(self.quests)  # 새로운 퀘스트 부여
            print(f"새로운 퀘스트: '{self.current_quest}'가 부여되었습니다!")

    def save_game(self):
        game_state = {
            "name": self.player.name,
            "health": self.player.health,
            "attack": self.player.attack,
            "level": self.player.level,
            "experience": self.player.experience,
            "inventory": self.player.inventory,
            "skills": self.player.skills,
            "gold": self.player.gold,
            "character_class": self.player.character_class,
            "quest": self.current_quest,
        }
        with open("save_game.json", "w") as f:
            json.dump(game_state, f)
        print("게임이 저장되었습니다.")

    def load_game(self):
        try:
            with open("save_game.json", "r") as f:
                game_state = json.load(f)
                self.player = Character(game_state["name"], game_state["health"], game_state["attack"], game_state["level"], game_state["character_class"])
                self.player.experience = game_state["experience"]
                self.player.inventory = game_state["inventory"]
                self.player.skills = game_state["skills"]
                self.player.gold = game_state["gold"]
                self.current_quest = game_state["quest"]
            print("게임이 로드되었습니다.")
        except FileNotFoundError:
            print("저장된 게임이 없습니다.")

    def start(self):
        print("1. 새 게임")
        print("2. 저장된 게임 로드")
        choice = input("선택하세요: ")
        if choice == '2':
            self.load_game()
        self.choose_character()
        self.player.inventory.append("치료제")  # 기본 아이템 추가
        self.player.inventory.append("경험치 병")  # 기본 아이템 추가
        self.current_quest = random.choice(self.quests)  # 새로운 퀘스트 부여
        print(f"현재 퀘스트: '{self.current_quest}'가 부여되었습니다!")
        self.create_enemies(random.randint(2, 5))  # 2에서 5 사이의 적 생성
        self.battle()
        self.save_game()

if __name__ == "__main__":
    game = Game()
    game.start()
