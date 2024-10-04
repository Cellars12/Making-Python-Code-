import random
import json

class Quest:
    def __init__(self, description, reward):
        self.description = description
        self.reward = reward
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"퀘스트 '{self.description}' 완료! 보상: {self.reward} 골드")
        return self.reward

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
        self.skill_unlocks = self.get_skill_unlocks()
        self.status_effects = []

    def get_skill_unlocks(self):
        if self.character_class == "전사":
            return {100: "분노", 200: "방패막기", 300: "돌진", 400: "전사비기"}
        elif self.character_class == "마법사":
            return {100: "냉기 마법", 200: "화염구", 300: "번개", 400: "원소 폭발"}
        return {}

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name}가 {damage}의 피해를 입었습니다! 남은 체력: {self.health}")

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        print(f"{self.name}가 {enemy.name}를 공격합니다! {damage}의 피해를 입혔습니다.")
        enemy.take_damage(damage)

    def apply_status_effect(self, effect):
        self.status_effects.append(effect)
        print(f"{self.name}가 '{effect}' 상태 효과에 걸렸습니다!")

    def update_status_effects(self):
        for effect in list(self.status_effects):
            if effect == "중독":
                damage = random.randint(5, 10)
                self.take_damage(damage)
                print(f"{self.name}가 중독으로 {damage}의 피해를 입었습니다!")
            # 추가 상태 효과를 여기서 처리할 수 있습니다.

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name}가 {amount} 경험치를 얻었습니다! 총 경험치: {self.experience}")
        if self.experience >= 100:  # 레벨업 조건
            self.level_up()

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack += 5
        self.experience = 0
        print(f"{self.name}가 레벨 {self.level}로 상승했습니다! 체력: {self.health}, 공격력: {self.attack}")
        if self.level in self.skill_unlocks:
            self.learn_skill(self.skill_unlocks[self.level])

    def learn_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"{self.name}가 스킬 '{skill}'을(를) 배웠습니다!")

    def show_stats(self):
        print(f"이름: {self.name}, 직업: {self.character_class}, 레벨: {self.level}, "
              f"체력: {self.health}, 공격력: {self.attack}, 경험치: {self.experience}, "
              f"골드: {self.gold}, 인벤토리: {self.inventory}, 스킬: {self.skills}")

class Enemy(Character):
    def __init__(self, name, health, attack, special_ability=None):
        super().__init__(name, health, attack)
        self.special_ability = special_ability

    def use_special_ability(self, player):
        if self.special_ability == "독":
            damage = random.randint(5, 10)
            player.take_damage(damage)
            print(f"{self.name}가 독을 사용했습니다! {damage}의 피해를 입었습니다.")

class Shop:
    def __init__(self):
        self.items = {
            "치료제": 20,
            "경험치 병": 50,
            "강화 포션": 100,
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
        self.quest = None
        self.quest_completed = False
        self.shop = Shop()

    def create_quest(self):
        self.quest = Quest("고블린 2마리 처치하기", 50)

    def create_enemies(self, count):
        enemy_types = [
            ("고블린", random.randint(50, 80), random.randint(5, 10), "독"),
            ("슬라임", random.randint(30, 60), random.randint(3, 8)),
            ("늑대", random.randint(40, 70), random.randint(8, 12)),
        ]
        for _ in range(count):
            enemy_type = random.choice(enemy_types)
            enemy = Enemy(enemy_type[0], enemy_type[1], enemy_type[2], enemy_type[3] if len(enemy_type) > 3 else None)
            self.enemies.append(enemy)
            print(f"{enemy.name}가 나타났습니다! 체력: {enemy.health}, 공격력: {enemy.attack}")

    def battle(self):
        if self.quest and not self.quest.completed:
            print(f"현재 퀘스트: {self.quest.description}")

        while self.player.is_alive() and self.enemies:
            self.player.update_status_effects()
            action = input("행동을 선택하세요 (1: 공격, 2: 아이템 사용, 3: 스킬 사용, 4: 상점, 5: 스탯 보기): ")
            if action == '1':
                for enemy in list(self.enemies):
                    self.player.attack_enemy(enemy)
                    if not enemy.is_alive():
                        print(f"{enemy.name}가 쓰러졌습니다!")
                        self.player.gain_experience(50)
                        self.player.add_gold(random.randint(5, 20))
                        self.enemies.remove(enemy)
                        if self.quest and not self.quest.completed and len(self.enemies) == 0:
                            self.quest.complete()
                            self.player.add_gold(self.quest.reward)
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
            elif action == '5':
                self.player.show_stats()
            else:
                print("잘못된 선택입니다.")

            print("")

        if self.player.is_alive() and len(self.enemies) == 0:
            print("축하합니다! 모든 적을 처치했습니다!")

    def use_item(self):
        if self.player.inventory:
            print("사용할 아이템을 선택하세요:")
            for idx, item in enumerate(self.player.inventory, start=1):
                print(f"{idx}. {item}")
            choice = int(input("아이템 번호를 입력하세요: ")) - 1
            if 0 <= choice < len(self.player.inventory):
                item_to_use = self.player.inventory[choice]
                if item_to_use == "치료제":
                    self.player.health += 30
                    self.player.inventory.remove(item_to_use)
                    print(f"{self.player.name}가 {item_to_use}를 사용하여 체력을 30 회복했습니다! 남은 체력: {self.player.health}")
                elif item_to_use == "경험치 병":
                    xp_gain = random.randint(10, 50)
                    self.player.gain_experience(xp_gain)
                    self.player.inventory.remove(item_to_use)
                    print(f"{self.player.name}가 {item_to_use}를 사용하여 {xp_gain} 경험치를 얻었습니다!")
                else:
                    print(f"{item_to_use}는 사용할 수 없는 아이템입니다.")
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
                target_enemy = random.choice(self.enemies)  # 랜덤으로 적을 선택
                damage = random.randint(15, self.player.attack + 10)
                print(f"{self.player.name}가 스킬 '{self.player.skills[choice]}'로 {target_enemy.name}를 공격합니다! {damage}의 피해를 입혔습니다.")
                target_enemy.take_damage(damage)
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

    def start(self):
        print("1. 새 게임")
        print("2. 저장된 게임 로드")
        choice = input("선택하세요: ")
        if choice == '2':
            self.load_game()
        self.choose_character()
        self.player.inventory.append("치료제")  # 기본 아이템 추가
        self.create_quest()  # 기본 퀘스트 추가
        self.create_enemies(random.randint(2, 5))  # 2에서 5 사이의 적 생성
        self.battle()

    def choose_character(self):
        print("캐릭터를 선택하세요:")
        print("1. 전사 (체력: 100, 공격력: 20)")
        print("2. 마법사 (체력: 80, 공격력: 30)")
        
        choice = input("캐릭터 번호를 입력하세요: ")
        if choice == '1':
            self.player = Character("전사", 100, 20, character_class="전사")
        elif choice == '2':
            self.player = Character("마법사", 80, 30, character_class="마법사")
        else:
            print("잘못된 선택입니다. 전사로 설정합니다.")
            self.player = Character("전사", 100, 20, character_class="전사")

if __name__ == "__main__":
    game = Game()
    game.start()
